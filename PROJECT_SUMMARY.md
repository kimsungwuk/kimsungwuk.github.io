# Project Briefing: Finder B2B CRM

## Summary for Local Agent
This is a B2B Customer Relationship Management (CRM) project named "Finder B2B CRM" (Growth CRM). It is built with Next.js 14 (App Router) and aims to provide features for startup agility and enterprise-level management.

## Key Features Implemented (Phase 3)
- **Sales Pipeline:** A visual Kanban board using `dnd-kit` for deal management (Lead -> Meeting -> Proposal -> Contract).
- **Map Explorer:** A GIS view for visualizing customer locations (mocked for demo, ready for Google Maps API).
- **OCR Scan:** Business card recognition using `tesseract.js` to extract contact info.
- **RBAC Auth:** Role-Based Access Control using NextAuth.js (Admin/Manager/Member).
- **Stats Dashboard:** Real-time metrics visualization (using fallback mock data due to local DB connectivity).

## Current Project State
- **Root Path:** `/Users/kimsungwuk/.openclaw/workspace/projects/finder-b2b-crm/`
- **Frontend:** Next.js 14+, Tailwind CSS, Shadcn UI.
- **Backend:** Next.js API Routes, Prisma ORM.
- **Auth Mode:** Currently in "Mock Mode" for stable demo access.
  - **ID:** `admin@finder.com`
  - **PW:** `admin123`
- **Database:** PostgreSQL/PostGIS (Configuration ready in schema, but local service was unreachable during remote session).

## Next Steps Planned
1. Connect to a live PostgreSQL instance and run `npx prisma migrate dev`.
2. Finalize real Google Maps API integration.
3. Enhance mobile responsiveness for the Kanban board.
