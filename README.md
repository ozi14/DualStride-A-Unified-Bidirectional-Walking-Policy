# DualStride: A Unified Bidirectional Walking Policy for the Unitree G1 Humanoid

**Authors:** Taha Oğuzhan Uçar, Enis Özden  
**Institution:** Department of Computer Science, Binghamton University  
**Course:** Intelligent Mobile Robotics, Spring 2025  
**Advisor:** Prof. Shiqi Zhang

---

## 📘 Overview

DualStride introduces a single reinforcement learning (RL) policy capable of controlling a humanoid robot to walk both forward and backward.
Unlike traditional locomotion systems that require separate controllers for each direction, DualStride achieves bidirectional walking within one neural network, improving efficiency, robustness, and training scalability.

---

## 🎯 Motivation

Humanoid robots need to navigate human-scale environments — warehouses, hospitals, and homes — where reverse motion is critical for safety and flexibility.
DualStride addresses this by:
- Eliminating controller-switch delays,
- Reducing training and validation overhead,
- Enabling generalizable bidirectional locomotion on the Unitree G1 platform.

---

## ⚙️ System Architecture

DualStride is built around a four-layer architecture:
1. **Simulation & Sensing** – 2048 parallel environments in NVIDIA Isaac Gym for high-throughput training.
2. **Control Core** – Real-time inference with joint-limit and energy safety filters.
3. **Learning Engine** – PPO-based reinforcement learning with curriculum scheduling.
4. **Ops & Tooling** – Automated CI pipeline, TensorRT deployment, and visualization dashboards.

---

## 🧠 Key Design Features

- **Symmetric Reward Function**: Mirrors gait metrics to encourage forward and backward generalization.
- **Curriculum Learning**: Gradually flips velocity signs to train bidirectional movement without dual policies.
- **Domain Randomization**: Increases robustness to sensor noise, latency, and dynamic environments.
- **Safety-Aware Constraints**: Implements ISO TS 15066 joint and velocity limits.

---

## 📈 Results

| Metric | Target | Achieved |
|--------|--------|----------|
| RMS Velocity Error | ≤ 0.08 m/s | 0.05 m/s |
| Push-Recovery Success | ≥ 90% | 95% |
| Policy Latency | < 6 ms | 4.1 ms |
| Energy per meter (Forward/Backward) | < 65 J/kg·m | 61 / 68 J/kg·m |

✅ Demonstrated stable forward and backward walking  
✅ Achieved gait symmetry without handcrafted logic  
✅ Maintained real-time inference performance on Jetson Orin

---

## 🧩 Future Work

- Extend policy to omni-directional and dynamic terrain walking.
- Integrate arm motion for full-body balance.
- Deploy policy to real Unitree G1 hardware using ONNX/TensorRT.
- Explore meta-RL for online adaptation.

---

## 🧰 Tools and Frameworks

- **Simulator**: NVIDIA Isaac Gym
- **Algorithm**: Proximal Policy Optimization (PPO)
- **Frameworks**: PyTorch, Hydra, TensorRT
- **Hardware**: RTX 3070 Ti GPU
- **Visualization**: Grafana + Prometheus

---

## 📎 References

1. Rudin et al., *Learning to Walk in Minutes Using Massively Parallel Deep RL* (CoRL 2022)
2. Unitree Robotics, [unitree-rl GitHub Repository](https://github.com/unitreerobotics/unitree_rl_gym) (2023)
3. NVIDIA AI Robotics, Legged Gym G1 Simulation Suite (2024)
4. Kim et al., *Symmetry-Aware Curriculum RL for Reversible Gait Synthesis* (ICRA 2023)

---

## 🔗 Links

- **Report PDF**: [unified_bidirectional_walking.pdf](./unified_bidirectional_walking.pdf)
- **Unitree RL Repository**: [GitHub](https://github.com/unitreerobotics/unitree_rl_gym)
- **NVIDIA Isaac Gym**: [Developer Blog](https://developer.nvidia.com/isaac-gym)

---

## 📄 License

This project is part of academic coursework at Binghamton University. Please contact the authors for usage permissions.

