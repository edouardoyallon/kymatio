import os
import io
import tensorflow as tf
from kymatio.scattering2d import Scattering2D
import torch
import numpy as np
import pytest
from kymatio.backend.fake_backend import backend as fake_backend

class TestScattering2DTensorflow:
    def reorder_coefficients_from_interleaved(self, J, L):
        # helper function to obtain positions of order0, order1, order2 from interleaved
        order0, order1, order2 = [], [], []
        n_order0, n_order1, n_order2 = 1, J * L, L ** 2 * J * (J - 1) // 2
        n = 0
        order0.append(n)
        for j1 in range(J):
            for l1 in range(L):
                n += 1
                order1.append(n)
                for j2 in range(j1 + 1, J):
                    for l2 in range(L):
                        n += 1
                        order2.append(n)
        assert len(order0) == n_order0
        assert len(order1) == n_order1
        assert len(order2) == n_order2
        return order0, order1, order2

    def test_Scattering2D(self):
        test_data_dir = os.path.dirname(__file__)
        data = None
        with open(os.path.join(test_data_dir, 'test_data_2d.pt'), 'rb') as f:
            buffer = io.BytesIO(f.read())
            data = torch.load(buffer)

        x = data['x'].numpy()
        S = data['Sx'].numpy()
        J = data['J']

        # we need to reorder S from interleaved (how it's saved) to o0, o1, o2
        # (which is how it's now computed)

        o0, o1, o2 = self.reorder_coefficients_from_interleaved(J, 8)
        reorder = np.concatenate((o0, o1, o2))
        S = S[..., reorder, :, :]

        pre_pad = data['pre_pad']
        M, N = x.shape[2:]

        # Tf
        scattering = Scattering2D(J, shape=(M, N), pre_pad=pre_pad, frontend='tensorflow')
        Sg = scattering(x)

        assert np.allclose(Sg, S)

    def test_inputs(self):
        with pytest.raises(RuntimeError) as ve:
            scattering = Scattering2D(2, shape=(10, 10), frontend='tensorflow', backend=fake_backend)
        assert 'not supported' in ve.value.args[0]

        with pytest.raises(RuntimeError) as ve:
            scattering = Scattering2D(10, shape=(10, 10), frontend='tensorflow')
        assert 'smallest dimension' in ve.value.args[0]