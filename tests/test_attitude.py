"""
    Copyright (C) 2017  GWU Flight Dynamics and Control Laboratory 

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import numpy as np
from .. import attitude


class TestHatAndVeeMap():
    x = np.random.rand(3)
    y = np.random.rand(3)

    def test_hat_map_zero(self):
        np.testing.assert_allclose(attitude.hat_map(self.x).dot(self.x), np.zeros(3))

    def test_hat_map_skew_symmetric(self):
        np.testing.assert_allclose(attitude.hat_map(self.x).T, -attitude.hat_map(self.x))

    def test_hat_vee_map_inverse(self):
        np.testing.assert_allclose(attitude.vee_map(attitude.hat_map(self.x)), self.x)

    def test_hat_map_cross_product(self):
        np.testing.assert_allclose(attitude.hat_map(self.x).dot(self.y), np.cross(self.x, self.y))
        np.testing.assert_allclose(attitude.hat_map(self.x).dot(self.y), -attitude.hat_map(self.y).dot(self.x))      


class TestEulerRot():
    angle = (2*np.pi - 0) * np.random.rand(1) + 0

    def test_rot1_orthogonal(self):
        mat = attitude.rot1(self.angle)
        np.testing.assert_array_almost_equal(mat.T.dot(mat), np.eye(3, 3))

    def test_rot2_orthogonal(self):
        mat = attitude.rot2(self.angle)
        np.testing.assert_array_almost_equal(mat.T.dot(mat), np.eye(3, 3))

    def test_rot3_orthogonal(self):
        mat = attitude.rot3(self.angle)
        np.testing.assert_array_almost_equal(mat.T.dot(mat), np.eye(3, 3))

    def test_rot1_determinant_1(self):
        mat = attitude.rot1(self.angle)
        np.testing.assert_allclose(np.linalg.det(mat), 1)

    def test_rot2_determinant_1(self):
        mat = attitude.rot2(self.angle)
        np.testing.assert_allclose(np.linalg.det(mat), 1)

    def test_rot3_determinant_1(self):
        mat = attitude.rot3(self.angle)
        np.testing.assert_allclose(np.linalg.det(mat), 1)


class TestEulerRot90_column():
    angle = np.pi/2
    b1 = np.array([1, 0, 0])
    b2 = np.array([0, 1, 0])
    b3 = np.array([0, 0, 1])

    R1 = attitude.rot1(angle, 'c')
    R2 = attitude.rot2(angle, 'c')
    R3 = attitude.rot3(angle, 'c')

    def test_rot1_90_b1(self):
        np.testing.assert_array_almost_equal(self.R1.dot(self.b1), self.b1)

    def test_rot1_90_b2(self):
        np.testing.assert_array_almost_equal(self.R1.dot(self.b2), self.b3)

    def test_rot1_90_b3(self):
        np.testing.assert_array_almost_equal(self.R1.dot(self.b3), -self.b2)

    def test_rot2_90_b1(self):
        np.testing.assert_array_almost_equal(self.R2.dot(self.b1), -self.b3)

    def test_rot2_90_b2(self):
        np.testing.assert_array_almost_equal(self.R2.dot(self.b2), self.b2)

    def test_rot2_90_b3(self):
        np.testing.assert_array_almost_equal(self.R2.dot(self.b3), self.b1)

    def test_rot3_90_b1(self):
        np.testing.assert_array_almost_equal(self.R3.dot(self.b1), self.b2)

    def test_rot3_90_b2(self):
        np.testing.assert_array_almost_equal(self.R3.dot(self.b2), -self.b1)

    def test_rot3_90_b3(self):
        np.testing.assert_array_almost_equal(self.R3.dot(self.b3), self.b3)
    