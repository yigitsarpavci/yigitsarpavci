# Yiğit Sarp Avcı

I am a Computer Engineering student at **Boğaziçi University** and Backend Developer Intern at **DefineX**, previously interning at **Akbank** (SRE) and **Smash Mate** (Software Engineering).

My focus spans the entire computing stack—from low-level systems programming and processor architecture to scalable enterprise backends and algorithmic FinTech platforms—combining strong theoretical computer science foundations with modern, AI-assisted product development.

---

### Education

- **Boğaziçi University** — B.Sc. in Computer Engineering *(09/2023 – Expected 06/2028 · GPA: 2.93/4.00)*
  - **Extracurriculars & Athletics:** Executive Board Member & DJ at Radyo Boğaziçi; Regional Organizational Team Member at ESTIEM; Work and Travel USA participant; Student-Athlete (sailing, skiing & windsurfing).
  - **Volunteering & Mentorship:** Volunteering Division Member at Industrial Engineering Club (BÜYAK); educational mentor to high school students.
- **Kabataş Boys' High School** *(09/2018 – 06/2023 · GPA: 3.78/4.00)*
  - **Extracurriculars:** Debate, Model United Nations (MUN), Entrepreneurship, and Coding Clubs.
  - **Volunteering:** Community Involvement Projects Club and TOÇEV (Tüvana Okuma İstekli Çocuk Eğitim Vakfı).

---

### Experience

- **Backend Developer Intern** — **DefineX** *(09/2026 – Present)*
  - Contributing to backend development, scalable enterprise software solutions, RESTful API design, and system optimizations across enterprise environments.
- **Site Reliability Engineering Intern** — **Akbank** *(07/2026 – 09/2026)*
  - Contributed to the reliability, scalability, and performance of mission-critical banking infrastructure within the SRE team. Engaged in Linux systems engineering, operational monitoring, and high-availability systems management.
- **Software Engineering Intern** — **Smash Mate** *(06/2026 – 07/2026)*
  - Contributed to a microservices backend (**Java**, **Quarkus**) and a cross-platform mobile frontend application (**React Native**) during the pre-launch phase. Developed core backend features, authored comprehensive unit and integration tests to ensure zero-defect deployments, and actively participated in agile workflows, code reviews, and performance optimizations directly supporting the product's official launch.

---

### Technical Skills

- **Programming Languages:** Python, Java, C (C11), C++ (C++17), TypeScript, JavaScript, SQL, x86-64 Assembly, RISC-V Assembly, Bash
- **Backend & Systems:** Quarkus, FastAPI, Express, Microservices Architecture, RESTful APIs, WebSockets, Linux Syscalls, POSIX IPC, Multithreading (Pthreads)
- **Frontend & Mobile:** Next.js (App Router), React, React Native, Expo, WebAssembly (WASM), Tailwind CSS, Zustand
- **Databases & Storage:** PostgreSQL, SQLite, Redis, Prisma ORM, TypeORM, SQLAlchemy
- **DevOps, Testing & Tools:** Docker, Docker Compose, Linux/Unix, Git/GitHub, CI/CD (GitHub Actions), Jest, Pytest, CMake, Make

---

### Projects

#### Administrative & Enterprise Systems

- **[Restaurant Floor Plan SaaS](https://github.com/yigitsarpavci/seated)** — Multi-Tenant Table Management & Live-Ops Platform
  - Multi-tenant SaaS platform with slug-based tenant isolation (`/manage/[tenantSlug]`), interactive drag-and-drop floor plan builder (`react-rnd`), and real-time coordinate persistence.
  - Features a live-ops console for waitstaff with walk-in queues and multi-table merging, powered by Zustand global state and end-to-end Zod validation.
  - **Tech Stack:** `Next.js 16`, `TypeScript`, `Prisma`, `PostgreSQL`, `Zustand`, `Tailwind CSS`, `react-rnd`, `Zod`

- **[Enterprise Admin Dashboard](https://github.com/yigitsarpavci/Performo-Enterprise-Admin)** — Internal Operations & Role-Based Access Control Console
  - Full-stack admin portal featuring an ergonomic 3-column layout with Framer Motion micro-animations and real-time server-rendered operational analytics via Recharts.
  - Enforces granular RBAC (Admin/User) through custom HTTP-only JWT cookies (`jose`), bcrypt hashing, user directory workflows, and self-deletion safeguards.
  - **Tech Stack:** `Next.js 16`, `TypeScript`, `Prisma`, `SQLite`, `Tailwind CSS`, `Framer Motion`, `Recharts`, `jose (JWT)`, `bcryptjs`

- **[Full-Stack FAQ Module](https://github.com/yigitsarpavci/faq-project)** — Knowledge Base & REST Microservice
  - Decoupled FAQ architecture pairing a Next.js App Router frontend with an Express REST API, SQLite (`better-sqlite3`), TypeORM, database indexing, and SWR optimistic UI updates.
  - Secured via Next-Auth RBAC and server-side `express-validator`, backed by comprehensive test coverage using Jest, React Testing Library, and Supertest.
  - **Tech Stack:** `Next.js`, `Express`, `TypeORM`, `SQLite (better-sqlite3)`, `SWR`, `Next-Auth`, `Tailwind CSS`, `Jest`, `Supertest`, `express-validator`

#### Systems Programming & Computer Architecture

- **[CoreMark Performance Profiling](https://github.com/yigitsarpavci/CoreMark-Workload-Profiling)** — Architectural Benchmark & Compiler Optimization Study
  - Evaluated EEMBC CoreMark v1.0 throughput, instruction counts, and compiler vectorization across Apple Silicon (M2 ARM64) and RISC-V (CORE-V Wally) from `-O0` to `-Ofast` (`-march=native`).
  - Analyzed hardware vs. software multiply/divide and code density across RISC-V ISA extensions (RV32I, RV32IM, RV32IMC, RV32GC, RV64I), using automated Python and Bash benchmarking harnesses.
  - **Tech Stack:** `C11`, `RISC-V (RV32I/IM/IMC/GC, RV64I)`, `EEMBC CoreMark`, `GNU Toolchain`, `Clang/LLVM`, `Python`, `Bash`

- **[Bare-Metal RISC-V Simulator](https://github.com/yigitsarpavci/Solar-Escape-RISCV-Navigator)** — Bare-Metal RV32I Flight Pathfinding on Spike Simulator
  - Bare-metal RV32I Assembly flight pathfinding simulation executing directly on the Spike ISA Simulator without an operating system or standard library.
  - Configures memory layouts via custom linker scripts (`.ld`) segmenting ROM (`0x80000000`) and RAM (`0x80010000`), featuring a custom HTIF console driver, manual ABI stack framing, and fuel-constrained airport routing.
  - **Tech Stack:** `RISC-V Assembly (RV32I)`, `Spike ISA Simulator`, `GNU as / ld`, `Custom Linker Scripts (.ld)`, `HTIF Driver`

- **[x86-64 CPU Scheduler](https://github.com/yigitsarpavci/SchedSim-CPU-Scheduler)** — Zero-Libc Linux Process Scheduling Simulator
  - Zero-libc Linux CPU scheduling engine in pure x86-64 assembly implementing FCFS, SJF, SRTF, Priority First, and Round Robin via direct kernel syscalls (`sys_read`, `sys_write`, `sys_open`, `sys_exit`).
  - Features manual ASCII-to-integer parsing, buffer management, and PCB register tracking, validated against edge cases using an automated Python test harness.
  - **Tech Stack:** `x86-64 GNU Assembly`, `Linux Syscalls`, `GNU Toolchain (as, ld)`, `Make`, `Python Grader`

- **[Linux IPC Game Subsystem](https://github.com/yigitsarpavci/Space-Shooter-IPC-Controller)** — Real-Time POSIX IPC Subsystem & Game Architecture
  - Real-time 60 FPS terminal game architecture cleanly decoupling engine execution from input controllers via non-blocking named pipes (`O_NONBLOCK` FIFOs) and POSIX signals (`SIGUSR1`, `SIGTERM`).
  - Supports runtime controller hot-swapping via dynamic library loading (`dlopen`/`dlsym`), with monotonic frame timing (`clock_gettime`), lock-free circular ring buffers, and process lifecycle management (`fork`/`exec`, `waitpid`).
  - **Tech Stack:** `C11`, `Linux / POSIX.1-2008`, `Named Pipes (FIFOs)`, `POSIX Signals`, `dlopen / dlsym`, `Pthreads`, `Make`

- **[Functional Language Interpreter](https://github.com/yigitsarpavci/Aura-Functional-Interpreter)** — Multi-Paradigm Functional Language Interpreter
  - Custom functional language interpreter built in standard Python 3 with zero external dependencies, supporting first-class closures, currying, higher-order functions, and recursive AST evaluation.
  - Features a switchable dual-scoping execution engine (lexical vs. dynamic scoping via `--scope static`/`--scope dynamic`), source-coordinate error reporting, and automated regression test suites.
  - **Tech Stack:** `Python 3`, `AST Parsing`, `Language Design`, `Functional Programming Principles`, `Dual Scoping`

- **[Unix Command Interpreter](https://github.com/yigitsarpavci/Spireslayer-Command-Interpreter)** — C-Based Unix Shell with Backtracking Parser
  - Unix shell and command interpreter engineered in C11, featuring a custom recursive descent parser with grammar backtracking for complex tokenized command sequences.
  - Modular pipeline cleanly decoupling parsing, state management, and command execution, verified with strict GCC flags (`-std=c11 -Wall -Wextra -pedantic`) and automated I/O redirection test suites.
  - **Tech Stack:** `C11`, `GNU Make`, `GCC Toolchain`, `Grammar Backtracking`, `POSIX / Unix Shell`

#### Mobile & Game Development

- **[React Native Minesweeper](https://github.com/yigitsarpavci/smash-mate-minesweeper)** — Mobile Minesweeper with Iterative BFS & Expo Haptics
  - Mobile Minesweeper game built with React Native and Expo, featuring hardware-accelerated animations via `react-native-reanimated`, Glassmorphism blur effects (`expo-blur`), and custom synthesized 16-bit PCM audio feedback with Expo haptics.
  - Implements an iterative BFS flood-fill algorithm preventing call-stack overflows, safe-first-click generation, and pure reducer-driven state architecture (`useReducer`).
  - **Tech Stack:** `React Native`, `Expo`, `TypeScript`, `Reanimated`, `Expo Haptics & Audio`, `AsyncStorage`, `Iterative BFS`

- **[2048 WebAssembly Game](https://github.com/yigitsarpavci/qt-2048-wasm)** — C++/Qt6 Implementation Compiled to WebAssembly · [Live Demo](https://yigitsarpavci.github.io/qt-2048-wasm/)
  - Cross-platform 2048 puzzle game engineered in C++17 and Qt 6, compiled to WebAssembly via Emscripten and CMake for near-native browser performance, with automated GitHub Pages deployment.
  - Implements canonical directional grid normalization, an infinite undo history stack (`std::stack`) with deep-copy state snapshots, browser key-event filtering, and a timed Hard Mode.
  - **Tech Stack:** `C++17`, `Qt 6`, `WebAssembly (WASM)`, `CMake`, `Emscripten`, `std::stack`, `GitHub Actions`

- **[State-Machine Card Game](https://github.com/yigitsarpavci/Nightpass-A-Survival-Card-Game)** — State-Machine-Driven Survival Card Game
  - Terminal-based survival card game engineered in Java for CMPE 250, driven by a deterministic Finite State Machine (FSM) governing turn phases, encounters, and state loops.
  - Balances player stamina and health scaling across sequential phases using queue-based event deck randomization, backed by automated difficulty modeling test suites.
  - **Tech Stack:** `Java`, `Finite State Machines (FSM)`, `Object-Oriented Design`, `Data Structures & Algorithms`

#### Data Structures & Graph Algorithms

- **[Graph Network Analyzer](https://github.com/yigitsarpavci/MatrixNet-The-Operator-s-Console)** — Network Topology & Fault-Tolerance Analyzer
  - Network topology analysis platform in Java for CMPE 250, detecting single points of failure in $O(V + E)$ linear time via Tarjan's Strongly Connected Components (SCC) and DFS articulation points.
  - Employs custom memory-efficient adjacency lists, traversal stacks, and visited bitsets, benchmarked across recursive and iterative traversal implementations.
  - **Tech Stack:** `Java`, `Graph Theory`, `Tarjan's Algorithm (SCC)`, `Articulation Points (DFS)`, `Network Optimization`

- **[Marketplace Matching Simulation](https://github.com/yigitsarpavci/GigMatch-Pro)** — Algorithmic Freelance Marketplace Simulation
  - Freelance marketplace matching simulation in Java dynamically assigning work orders via custom binary max-heaps with index tracking in $O(\log N)$ extraction time.
  - Integrates multi-factor composite scoring (skills, ratings, cancellation reliability, burnout penalties), top-$K$ queries, and custom open-addressing hash maps and dynamic arrays.
  - **Tech Stack:** `Java`, `Dynamic Max-Heaps / Priority Queues`, `Algorithm Design`, `Top-K Queries`, `Computational Complexity`

#### Full-Stack FinTech

- **[Algorithmic Trading Simulator](https://github.com/yigitsarpavci/AlphaTrigger-AI)** — Real-Time Quantitative Trading Terminal & Simulator
  - Quantitative trading engine running a V8 Risk-First strategy on a 2-second simulation loop with Z-Score mean reversion, dynamic volatility-adjusted sizing, and a 4-state exit machine.
  - Streams real-time order book depth, execution logs, and P&L metrics to a Next.js terminal UI via full-duplex FastAPI WebSockets, Celery task queues, Redis, and Docker.
  - **Tech Stack:** `Python 3.11+`, `FastAPI`, `Next.js 14`, `Redis`, `Celery`, `WebSockets`, `Z-Score Strategy`, `Docker`

- **[Financial Analytics Dashboard](https://github.com/yigitsarpavci/fintech-intelligence-platform)** — Full-Stack Finance Dashboard & Matching Engine
  - Educational full-stack personal finance and portfolio risk platform built with Next.js 14 (App Router), FastAPI, SQLAlchemy, Alembic, PostgreSQL (`psycopg2`), and Docker Compose.
  - Features a real-time continuous limit-order matching engine with bid/ask queues, partial fills, balance reconciliation, and portfolio volatility metrics, with CI/CD enforcing automated pytest suites.
  - **Tech Stack:** `Next.js 14`, `FastAPI`, `Python`, `PostgreSQL (psycopg2)`, `SQLAlchemy`, `Docker / Docker Compose`, `Pytest`, `GitHub Actions`

---

### Languages

- **Turkish:** Native · **English:** Advanced / Professional Working Proficiency · **German:** Beginner / Elementary

### Hobbies & Interests

- Sailing, Skiing, Windsurfing, Wakeboarding, Kiteboarding, Surfing, Bouldering, Running, Fitness, Traveling

### Resume

- **CV / Resume:** [View / Download (PDF)](./cv/cv.pdf)
