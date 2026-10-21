# Yiğit Sarp Avcı

I am a Computer Engineering student at **Boğaziçi University** and Backend Developer Intern at **DefineX**, previously interning at **Akbank** (SRE) and **Smash Mate** (Software Engineering).

My focus spans the entire computing stack—from low-level systems programming and processor architecture to scalable enterprise backends and algorithmic FinTech platforms—combining strong theoretical computer science foundations with modern, AI-assisted product development.

---

### Education

- **Boğaziçi University** — B.Sc. in Computer Engineering *(09/2023 – Expected 06/2028)*
  - **Extracurriculars & Athletics:** Executive Board Member & DJ at Radyo Boğaziçi; Regional Organizational Team Member at ESTIEM; Work and Travel USA participant; Student-Athlete (sailing, skiing & windsurfing).
  - **Volunteering & Mentorship:** Volunteering Division Member at Industrial Engineering Club (BÜYAK); Educational Mentor to high school students.
- **Kabataş Boys' High School** *(09/2018 – 06/2023 · GPA: 3.78/4.00)*
  - **Extracurriculars:** Debate, Model United Nations (MUN), Entrepreneurship, and Coding Clubs.
  - **Volunteering:** Community Involvement Projects Club and TOÇEV (Tüvana Okuma İstekli Çocuk Eğitim Vakfı).

---

### Experience

- **Backend Developer Intern** — **DefineX** *(09/2026 – Present)*
  - Developing internal data processing platforms and Model Context Protocol (MCP) integrations, streamlining operational workflows for corporate teams by automating enterprise data extraction and RESTful backend pipelines.
  - Leveraging modern AI-assisted engineering workflows to accelerate enterprise backend feature delivery, implementing robust data validation schemas and optimizing API request throughput.
- **Site Reliability Engineering Intern** — **Akbank** *(07/2026 – 09/2026)*
  - Maintained high availability for mission-critical core banking infrastructure by designing real-time observability dashboards and proactive alerting thresholds in Dynatrace and Grafana.
  - Engaged in Linux systems engineering, server health diagnostics, and log analysis to accelerate incident detection and root-cause resolution across high-throughput production nodes.
- **Software Engineering Intern** — **Smash Mate** *(06/2026 – 07/2026)*
  - Engineered player matchmaking, search discovery, and scoring microservices using Java (Quarkus), designing high-performance RESTful endpoints and core game-matching domain logic.
  - Developed responsive mobile interfaces in React Native and authored comprehensive unit and integration test suites, delivering a fully functional, zero-defect pre-launch release.

---

### Technical Skills

- **Programming Languages:** Python, Java, C (C11), C++ (C++17), TypeScript, JavaScript, SQL, x86-64 Assembly, RISC-V Assembly, Bash
- **Backend & Systems:** Quarkus, FastAPI, Express, Microservices Architecture, RESTful APIs, WebSockets, Linux Syscalls, POSIX IPC, Multithreading (Pthreads)
- **Frontend & Mobile:** Next.js (App Router), React, React Native, Expo, WebAssembly (WASM), Tailwind CSS, Zustand
- **Databases & Storage:** PostgreSQL, SQLite, Redis, Prisma ORM, TypeORM, SQLAlchemy
- **DevOps, Testing & Tools:** Docker, Docker Compose, Linux/Unix, Git/GitHub, CI/CD (GitHub Actions), Jest, Pytest, CMake, Make

---

### Projects

#### Full-Stack SaaS & Enterprise Backends

- **[Restaurant Floor Plan SaaS](https://github.com/yigitsarpavci/restaurant-floor-plan-saas)** — Multi-Tenant Table Management & Live-Ops Platform
  - Multi-tenant SaaS platform with slug-based tenant isolation (`/manage/[tenantSlug]`), interactive drag-and-drop floor plan builder (`react-rnd`), and real-time coordinate persistence.
  - Features a live-ops console for waitstaff with walk-in queues and multi-table merging, powered by Zustand global state and end-to-end Zod validation.
  - **Tech Stack:** `Next.js 16`, `TypeScript`, `Prisma`, `PostgreSQL`, `Zustand`, `Tailwind CSS`, `react-rnd`, `Zod`

- **[Enterprise Admin Dashboard](https://github.com/yigitsarpavci/enterprise-admin-dashboard)** — Internal Operations & Employee Task Management Console
  - Full-stack company operations console for delegating strategic employee tasks, tracking daily progress, and logging routine checklists and work hours.
  - Implements department-level productivity comparisons (Recharts), granular RBAC (Admin vs. User) via HTTP-only JWT cookies (`jose`), and user lifecycle workflows.
  - **Tech Stack:** `Next.js 16`, `TypeScript`, `Prisma`, `SQLite`, `Tailwind CSS`, `Framer Motion`, `Recharts`, `jose (JWT)`, `bcryptjs`

#### Quantitative FinTech & Real-Time Trading

- **[Algorithmic Trading Simulator](https://github.com/yigitsarpavci/algorithmic-trading-simulator)** — Real-Time Quantitative Trading Terminal & Simulator
  - Quantitative trading engine running a V8 Risk-First strategy on a 2-second simulation loop with Z-Score mean reversion, dynamic volatility-adjusted sizing, and a 4-state exit machine.
  - Streams real-time order book depth, execution logs, and P&L metrics to a Next.js terminal UI via full-duplex FastAPI WebSockets, Celery task queues, Redis, and Docker.
  - **Tech Stack:** `Python 3.11+`, `FastAPI`, `Next.js 14`, `Redis`, `Celery`, `WebSockets`, `Z-Score Strategy`, `Docker`

- **[Financial Analytics Dashboard](https://github.com/yigitsarpavci/financial-analytics-dashboard)** — Personal Finance & Portfolio Risk Platform
  - Educational full-stack personal finance and portfolio risk platform built with Next.js 14 (App Router), FastAPI, SQLAlchemy, Alembic, PostgreSQL (`psycopg2`), and Docker Compose.
  - Implements categorical cash-flow analytics, weighted multi-asset diversification scoring, and context-aware AI advisory insights via OpenAI with deterministic rule fallbacks.
  - **Tech Stack:** `Next.js 14`, `FastAPI`, `Python`, `PostgreSQL (psycopg2)`, `SQLAlchemy`, `Docker / Docker Compose`, `OpenAI API`, `Recharts`

#### Systems Programming & Computer Architecture

- **[Linux IPC Game Subsystem](https://github.com/yigitsarpavci/linux-ipc-game-subsystem)** — Real-Time POSIX IPC Subsystem & Game Architecture
  - Real-time 60 FPS terminal game architecture cleanly decoupling engine execution from input controllers via non-blocking named pipes (`O_NONBLOCK` FIFOs) and POSIX signals (`SIGUSR1`, `SIGTERM`).
  - Supports runtime controller hot-swapping via dynamic library loading (`dlopen`/`dlsym`), with monotonic frame timing (`clock_gettime`), lock-free circular ring buffers, and process lifecycle management (`fork`/`exec`, `waitpid`).
  - **Tech Stack:** `C11`, `Linux / POSIX.1-2008`, `Named Pipes (FIFOs)`, `POSIX Signals`, `dlopen / dlsym`, `Pthreads`, `Make`

- **[Low-Level Systems & Computer Architecture Lab](https://github.com/yigitsarpavci/low-level-systems-lab)** — Zero-Libc x86-64 Scheduler, Bare-Metal RISC-V, C11 Shell & CoreMark Benchmarking
  - Unified systems programming laboratory featuring a zero-libc x86-64 process scheduler (direct Linux syscalls), bare-metal RV32I flight pathfinding on Spike simulator (`.ld` memory mapping), and a modular C11 Unix shell with grammar backtracking.
  - Includes empirical EEMBC CoreMark profiling evaluating compiler optimization flags (`-O0` to `-Ofast`) and instruction-level parallelism (ILP) across Apple Silicon (M2 ARM64) and RISC-V extensions.
  - **Tech Stack:** `x86-64 Assembly`, `RISC-V (RV32I/IM/IMC/GC)`, `ARM64`, `C11`, `Linux Syscalls`, `Spike Simulator`, `Clang/LLVM`, `GNU Toolchain`

#### Algorithms & Data Structures

- **[Advanced Data Structures & Algorithms Suite](https://github.com/yigitsarpavci/data-structures-and-algorithms-suite)** — Graph Theory, Priority Allocators & State Machines
  - Curated Java algorithms suite implementing Tarjan's Strongly Connected Components (SCC) and articulation points in $O(V + E)$ linear time, dynamic freelance matching via indexed max-heaps in $O(\log N)$ time, and a deterministic survival card game engine.
  - Features custom memory-efficient adjacency lists, visited bitsets, open-addressing hash maps, and sequential queue-driven state machine architectures.
  - **Tech Stack:** `Java`, `Graph Theory (Tarjan SCC)`, `Dynamic Max-Heaps`, `Finite State Machines (FSM)`, `Complexity Modeling`

#### Mobile & WebAssembly

- **[Cross-Platform & WebAssembly Game Lab](https://github.com/yigitsarpavci/cross-platform-game-lab)** — C++/Qt6 WASM & React Native Mobile Architecture · [Live Demo](https://yigitsarpavci.github.io/2048-webassembly-game/)
  - Unified game engineering lab featuring a cross-platform 2048 puzzle engine engineered in C++17/Qt 6 compiled to WebAssembly via Emscripten, and an Expo/React Native Minesweeper mobile application.
  - Implements directional grid normalization, an infinite undo history stack (`std::stack`) with deep-copy snapshots, non-recursive iterative BFS flood-fill preventing call-stack overflows, and hardware haptics.
  - **Tech Stack:** `C++17`, `Qt 6`, `WebAssembly (WASM)`, `CMake`, `Emscripten`, `React Native`, `Expo`, `TypeScript`, `Iterative BFS`

---

### Languages

- **Turkish:** Native · **English:** Advanced / Professional Working Proficiency · **German:** Beginner / Elementary

### Hobbies & Interests

- Sailing, Skiing, Windsurfing, Wakeboarding, Kiteboarding, Surfing, Bouldering, Running, Traveling

### Resume

- **CV / Resume:** [View / Download (PDF)](./cv/cv.pdf)
