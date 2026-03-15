# Finder B2B CRM 아키텍처 및 폴더 구조 설계

## 1. 아키텍처 개요
Finder B2B CRM은 **Next.js (App Router)** 기반의 Full-stack 프레임워크를 사용하며, 확장성과 유지보수성을 위해 API-first 접근 방식을 취합니다.

- **Frontend/Backend:** Next.js 14+ (App Router)
- **Database:** PostgreSQL (with Prisma ORM or Drizzle)
- **Authentication:** NextAuth.js (RBAC 기반 권한 관리)
- **GIS:** Google Maps API
- **OCR:** Tesseract.js (또는 서버 사이드 Tesseract-OCR)
- **State Management:** TanStack Query (React Query) & Zustand
- **UI:** Tailwind CSS + Shadcn UI (Radix UI)

## 2. 폴더 구조 (Project Structure)

```text
finder-b2b-crm/
├── .github/                # GitHub Actions & CI/CD
├── public/                 # Static assets (images, icons, etc.)
├── src/
│   ├── app/                # Next.js App Router (Pages, Layouts, API Routes)
│   │   ├── (auth)/         # Login, Register, Password Reset
│   │   ├── (dashboard)/    # Main CRM Dashboard
│   │   │   ├── pipeline/   # Kanban Board
│   │   │   ├── companies/  # Company Management (Map & List)
│   │   │   ├── activities/ # Global Activity Logs
│   │   │   └── settings/   # Profile & Team Settings
│   │   └── api/            # RESTful API Endpoints
│   ├── components/         # Reusable UI Components
│   │   ├── ui/             # Shadcn UI primitives
│   │   ├── common/         # Layout components, Sidebar, Navbar
│   │   ├── pipeline/       # Kanban specific components
│   │   ├── map/            # Google Maps integration components
│   │   └── forms/          # Business logic forms (OCR integration)
│   ├── hooks/              # Custom React Hooks
│   ├── lib/                # Utility functions, Prisma Client, API Clients
│   ├── services/           # Business Logic / Data Fetching Layers
│   ├── store/              # Global state (Zustand)
│   ├── types/              # TypeScript definitions & Interfaces
│   └── styles/             # Global CSS & Tailwind config
├── prisma/                 # Database Schema & Migrations
├── tests/                  # Unit & E2E Tests
├── .env.example            # Environment variable templates
├── next.config.mjs         # Next.js configuration
├── tailwind.config.ts      # Tailwind configuration
└── tsconfig.json           # TypeScript configuration
```

## 3. 핵심 모듈 설계 방향
- **Pipeline:** `dnd-kit` 또는 `react-beautiful-dnd`를 활용한 칸반 보드 구현.
- **Maps:** `react-google-maps/api`를 사용하여 실시간 위치 기반 필터링 및 클러스터링.
- **OCR:** `tesseract.js`를 클라이언트 또는 서버(API Route)에서 실행하여 비정형 데이터 추출.
- **RBAC:** 미들웨어를 통해 User Role(Admin, Manager, Member)에 따른 페이지 및 API 접근 제어.
