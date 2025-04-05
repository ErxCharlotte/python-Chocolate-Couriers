# 🍫 Chocolate Couriers

A graph-based Python program simulating a courier communication network, where messages must pass through **at most one untrusted courier**.  

---

## 🗺️ Functionality

- Add/remove **vertices** and **edges**
- Update whether a courier is **trusted**
- `send_message(s, t)`: Finds a path from `s` to `t` with **≤ 1 untrusted node**
- `check_security(s, t)`: Returns semi-trusted edges that are **critical** for avoiding untrusted-only paths

---

## 📁 Files

- `vertex.py`: Defines each courier (vertex) with trust status and neighbor connections
- `graph.py`: Manages the overall graph and implements message sending and security checks

---

## ✅ Assumptions

- The graph is undirected and simple
- All inputs are valid (e.g. `s` and `t` are distinct and trusted)
- Modifications maintain graph consistency

---
