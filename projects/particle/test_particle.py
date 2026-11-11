print("--- SCRIPT START ---", flush=True)

import pytest
import pygame
import particle

@pytest.mark.parametrize("x0, y0, vx0, vy0", [
    (0, 0, 5, 10),
    (300, 200, -7, 12),
    (500, 300, -4, -10),
])

def test_particle_move(x0, y0, vx0, vy0):
    width, height = 600, 400
    dt, g = 2, 4
    w = particle.World(width, height, dt, g)

    p = particle.Particle((x0, y0), (vx0, vy0), w)
    N = 2000
    for i in range(N):
        p.update()
    assert p.x == x0 + vx0 * dt
    py_discrete = y0 + vy0 * (N * dt) + 1/2 * g * N * (N + 1) * dt ** 2
    assert p.y == y0 + (vy0 + g * dt)*dt
    py_continuous = y0 + vy0 * (N * dt) + 1/2 * g * N ** 2 * dt ** 2
    assert p.y == pytest.approx(py_continuous, 1e-3)