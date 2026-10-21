# Yiğit Sarp Avcı

I am a Computer Engineering student at Boğaziçi University with a deep passion for building software across the entire computing stack—from bare-metal systems and processor architecture to scalable enterprise backends, full-stack SaaS platforms, and algorithmic FinTech solutions.

Currently, I work as a Backend Developer Intern at DefineX, contributing to the architecture, RESTful API design, and optimization of enterprise-grade software systems. Previously, I gained hands-on industry experience as a Site Reliability Engineering (SRE) Intern at Akbank—where I focused on the high availability, Linux systems engineering, and performance of mission-critical banking infrastructure—and as a Software Engineering Intern at Smash Mate, developing core backend microservices (Java, Quarkus) and cross-platform mobile features (React Native) during a high-paced pre-launch phase.

My engineering approach combines strong theoretical computer science foundations with practical, AI-assisted product development across three core pillars:
- **Backend, Full-Stack & FinTech:** Designing multi-tenant SaaS applications, real-time trading simulators, and limit-order matching engines using Python (FastAPI), Java (Quarkus), TypeScript, Next.js, React Native, PostgreSQL, Redis, and Docker.
- **Systems Programming & Computer Architecture:** Engineering low-level solutions including Linux syscall-based CPU schedulers in x86-64 Assembly, bare-metal RISC-V navigation firmware, CoreMark compiler/ISA profiling, and asynchronous C11/POSIX IPC engines.
- **Algorithms & Language Design:** Building functional language and shell interpreters, graph topology analyzers (Tarjan's SCC), and priority-based allocation engines in Python, C, C++, and Java.

Beyond software engineering, I thrive in dynamic, collaborative environments. I serve as an Executive Board Member & DJ at Radyo Boğaziçi, a Regional Organizational Team Member at ESTIEM, and a Volunteering Division Member at BÜYAK, alongside providing educational mentorship to high school students. A former Work and Travel USA participant and an active student-athlete competing in sailing, skiing, and windsurfing, I also enjoy wakeboarding, kiteboarding, surfing, bouldering, running, fitness, and traveling.

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

- **Programming Languages:** Python, Java, C (C11), C++ (C++17), TypeScript, JavaScript, SQL, x86-64 Assembly, RISC-V Assembly (RV32I), Bash
- **Backend & Cloud:** Quarkus, FastAPI, Express, Microservices Architecture, RESTful APIs, WebSockets, High Availability, Celery
- **Frontend & Mobile:** Next.js 16 (App Router), React, React Native, Expo, WebAssembly (WASM), Tailwind CSS, Zustand
- **Databases & Storage:** PostgreSQL, SQLite, Redis, Prisma ORM, TypeORM
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
  - Analyzed hardware vs. software multiply/divide and code density across RV32I/IM/IMC/GC and RV64I, using automated Python and Bash benchmarking harnesses reflecting computer architecture and digital logic (FPGA/VHDL) principles.
  - **Tech Stack:** `C11`, `RISC-V (RV32I/IM/IMC/GC, RV64I)`, `EEMBC CoreMark`, `GNU Toolchain`, `Clang/LLVM`, `Python`, `Bash`, `Computer Architecture / FPGA Concepts`

- **[Bare-Metal RISC-V Simulator](https://github.com/yigitsarpavci/Solar-Escape-RISCV-Navigator)** — Bare-Metal RV32I Flight Pathfinding on Spike Simulator
  - Bare-metal RV32I Assembly flight pathfinding simulation executing directly on the Spike ISA Simulator without an operating system or standard library.
  - Configures memory layouts via custom linker scripts (`.ld`) segmenting ROM (`0x80000000`) and RAM (`0x80010000`), featuring a custom HTIF console driver, manual ABI stack framing, and greedy radiation avoidance.
  - **Tech Stack:** `RISC-V Assembly (RV32I)`, `Spike ISA Simulator`, `GNU as / ld`, `Custom Linker Scripts (.ld)`, `HTIF Driver`

- **[x86-64 CPU Scheduler](https://github.com/yigitsarpavci/SchedSim-CPU-Scheduler)** — Zero-Libc Linux Process Scheduling Simulator
  - Zero-libc Linux CPU scheduling engine in pure x86-64 assembly implementing FCFS, SJF, SRTF, Priority First, and Round Robin via direct kernel syscalls (`sys_read`, `sys_write`, `sys_open`, `sys_exit`).
  - Features manual ASCII-to-integer parsing, buffer management, and PCB register tracking, validated against edge cases using an automated Python test harness.
  - **Tech Stack:** `x86-64 GNU Assembly`, `Linux Syscalls`, `GNU Toolchain (as, ld)`, `Make`, `Process Scheduling (FCFS, SJF, SRTF, Priority, RR)`, `Python Grader`

- **[Linux IPC Game Subsystem](https://github.com/yigitsarpavci/Space-Shooter-IPC-Controller)** — Real-Time POSIX IPC Subsystem & Game Architecture
  - Real-time 60 FPS multi-process architecture decoupling physics from controllers via non-blocking named pipes (`O_NONBLOCK` FIFOs), POSIX signals (`SIGUSR1`, `SIGTERM`), and process lifecycle management (`fork`/`exec`, `waitpid`).
  - Supports hot-swapping manual and heuristic controller plugins at runtime via `dlopen`/`dlsym`, with monotonic timers (`clock_gettime`), lock-free circular ring buffers, and Pthreads synchronization.
  - **Tech Stack:** `C11`, `Linux / POSIX.1-2008`, `Named Pipes (FIFOs)`, `POSIX Signals`, `dlopen / dlsym`, `Pthreads`, `fork/exec & waitpid`, `Make`

- **[Functional Language Interpreter](https://github.com/yigitsarpavci/Aura-Functional-Interpreter)** — Multi-Paradigm Functional Language Interpreter
  - Custom interpreter in standard Python 3 inspired by Scheme/Racket functional semantics, supporting first-class closures, currying, higher-order functions, and recursive AST evaluation.
  - Features a switchable dual-scoping execution engine (lexical vs. dynamic scoping via `--scope static`/`--scope dynamic`), source-coordinate error reporting, and automated regression test suites.
  - **Tech Stack:** `Python 3`, `AST Parsing`, `Language Design`, `Functional Programming (Scheme/Racket Semantics)`, `Dual Scoping`

- **[Unix Command Interpreter](https://github.com/yigitsarpavci/Spireslayer-Command-Interpreter)** — C-Based Unix Shell with Backtracking Parser
  - Unix shell and command interpreter engineered in C11, featuring a custom recursive descent parser with grammar backtracking for complex tokenized command sequences.
  - Modular pipeline cleanly decoupling parsing, state management, and execution, verified with strict GCC flags (`-std=c11 -Wall -Wextra -pedantic`) and automated I/O redirection test suites.
  - **Tech Stack:** `C11`, `GNU Make`, `GCC Toolchain`, `Grammar Backtracking`, `POSIX / Unix Shell`

#### Mobile & Game Development

- **[React Native Minesweeper](https://github.com/yigitsarpavci/smash-mate-minesweeper)** — Mobile Minesweeper with Iterative BFS & Expo Haptics
  - Mobile Minesweeper with hardware-accelerated Reanimated graphics, Glassmorphism blur effects (`expo-blur`), safe-first-click generation, and custom synthesized 16-bit PCM audio feedback with Expo haptics.
  - Implements an iterative BFS flood-fill algorithm preventing call-stack overflows, backed by pure reducer-driven state architecture (`useReducer`).
  - **Tech Stack:** `React Native`, `Expo`, `TypeScript`, `Reanimated`, `Expo Haptics & Audio`, `AsyncStorage`, `Tailwind / NativeWind`, `Iterative BFS`

- **[2048 WebAssembly Game](https://github.com/yigitsarpavci/qt-2048-wasm)** — C++/Qt6 Implementation Compiled to WebAssembly · [Live Demo](https://yigitsarpavci.github.io/qt-2048-wasm/)
  - C++17/Qt6 game engine compiled to WebAssembly via Emscripten for near-native browser performance, featuring automated CI/CD deployment to GitHub Pages.
  - Implements canonical directional grid normalization, an infinite undo history stack (`std::stack`) with deep-copy snapshots, and timed Hard Mode.
  - **Tech Stack:** `C++17`, `Qt 6`, `WebAssembly (WASM)`, `CMake`, `Emscripten`, `std::stack`, `GitHub Actions`

- **[State-Machine Card Game](https://github.com/yigitsarpavci/Nightpass-A-Survival-Card-Game)** — State-Machine-Driven Survival Card Game
  - Terminal-based Java survival card game driven by a deterministic Finite State Machine (FSM) governing turn phases, encounters, combat loops, and rule-based logic.
  - Balances player stamina and health scaling via custom queue-based event deck randomization, backed by automated difficulty modeling test suites.
  - **Tech Stack:** `Java`, `Finite State Machines (FSM)`, `Object-Oriented Design`, `Rule-Based Logic & Algorithms`

#### Data Structures & Graph Algorithms

- **[Graph Network Analyzer](https://github.com/yigitsarpavci/MatrixNet-The-Operator-s-Console)** — Network Topology & Fault-Tolerance Analyzer
  - Java network topology analysis platform detecting single points of failure via Tarjan's Strongly Connected Components (SCC) and DFS articulation points in $O(V + E)$ linear time.
  - Employs custom memory-efficient adjacency structures, traversal stacks, and visited bitsets, benchmarked across recursive and iterative traversal implementations.
  - **Tech Stack:** `Java`, `Graph Theory`, `Tarjan's Algorithm (SCC)`, `Articulation Points (DFS)`, `Network Optimization`

- **[Marketplace Matching Simulation](https://github.com/yigitsarpavci/GigMatch-Pro)** — Algorithmic Freelance Marketplace Simulation
  - Enterprise marketplace matching simulation in Java dynamically assigning work orders via custom dynamic max-heaps in $O(\log N)$ extraction time.
  - Integrates multi-factor composite scoring (skills, ratings, burnout penalties), top-$K$ queries, and low-overhead open-addressing hash maps and dynamic arrays.
  - **Tech Stack:** `Java`, `Dynamic Max-Heaps / Priority Queues`, `Algorithm Design`, `Top-K Queries`, `Computational Complexity`

#### Full-Stack FinTech

- **[Algorithmic Trading Simulator](https://github.com/yigitsarpavci/AlphaTrigger-AI)** — Real-Time Quantitative Trading Terminal & Simulator
  - Quantitative trading engine executing a 2-second simulation loop with Z-Score mean reversion, volatility-adjusted position sizing, and trailing stop-losses.
  - Streams real-time order book depth and P&L metrics to a Next.js terminal UI via full-duplex FastAPI WebSockets, Celery task queues, Redis pub/sub, and Docker.
  - **Tech Stack:** `Python 3.11+`, `FastAPI`, `Next.js 14`, `Redis`, `Celery`, `WebSockets (Full-Duplex)`, `Z-Score Quantitative Strategy`, `Docker`

- **[Financial Analytics Dashboard](https://github.com/yigitsarpavci/fintech-intelligence-platform)** — Full-Stack Finance Dashboard & Matching Engine
  - Full-stack finance platform featuring a continuous limit-order book matching engine with bid/ask queues, partial fills, balance reconciliation, and PostgreSQL (`psycopg2`).
  - Provides algorithmic portfolio volatility analysis and an AI assistant, with Docker Compose and GitHub Actions CI/CD enforcing automated pytest suites.
  - **Tech Stack:** `Next.js 15+`, `FastAPI`, `Python`, `PostgreSQL (psycopg2)`, `Docker / Docker Compose`, `OpenAI API / NLP`, `Pytest`, `GitHub Actions`

---

### Languages

- **Turkish:** Native · **English:** Advanced / Professional Working Proficiency · **German:** Beginner / Elementary

### Hobbies & Interests

- Wakeboarding, Kiteboarding, Surfing, Bouldering, Running, Fitness, Traveling

---

### Contact

- **LinkedIn:** [linkedin.com/in/yigitsarpavci](https://www.linkedin.com/in/yigitsarpavci)
- **CV:** [View / Download](./cv/cv.pdf)
- **Email:** [yigit.avci@boun.edu.tr](mailto:yigit.avci@boun.edu.tr) · [yigitsarpavci@gmail.com](mailto:yigitsarpavci@gmail.com)
