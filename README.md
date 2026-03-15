# Finder B2B CRM

## Project Setup Progress

- [x] Project Initialization (Next.js 14)
- [x] Core Dependencies Installation (Prisma, TanStack Query, Zustand, etc.)
- [x] DB Schema Design & Prisma Setup
- [x] Prisma Client Instance Creation
- [x] NextAuth.js v5 Beta Setup & Middleware
- [x] App Router Structure ((auth), (dashboard) groups)
- [ ] Base Layout & Navigation
- [ ] Company Management (Map View)
- [ ] Pipeline (Kanban Board)
- [ ] Activity Log & OCR Integration

## How to Run

1. Clone or navigate to the project directory.
2. Install dependencies: `npm install`
3. Copy `.env.example` to `.env` and fill in `DATABASE_URL` and `AUTH_SECRET`.
4. Generate Prisma client: `npx prisma generate`
5. Run development server: `npm run dev`
