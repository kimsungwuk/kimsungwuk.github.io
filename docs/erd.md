# Finder B2B CRM DB 스키마 (ERD) 설계

Finder B2B CRM은 PostgreSQL을 사용하여 관계형 데이터를 저장하며, RBAC(권한 관리) 및 영업 데이터 간의 관계를 정의합니다.

## 1. ERD 개요 (Database Schema)

### 1.1. 사용자 및 조직 (User & Auth)
- `users`: 사용자 정보 (NextAuth Integration)
- `roles`: 사용자 권한 (ADMIN, MANAGER, MEMBER)
- `teams`: 조직/팀 구분

### 1.2. 고객사 및 연락처 (Account & Contact)
- `companies`: 고객사 (Account) 정보 (주소, GIS 좌표 포함)
- `contacts`: 개별 담당자 정보 (명함 OCR 데이터 포함)

### 1.3. 영업 기회 및 파이프라인 (Deal & Pipeline)
- `pipelines`: 영업 파이프라인 단계 (Lead, Meeting, Proposal, Contract)
- `deals`: 개별 영업 기회 (영업 가치, 단계 정보 등)

### 1.4. 활동 및 히스토리 (Activity & History)
- `activities`: 활동 로그 (Call, Meeting, Email, Note)
- `attachments`: 활동에 첨부된 파일 (OCR 원본 명함 이미지 등)

---

## 2. 상세 테이블 명세 (Prisma Schema Style)

```prisma
// This is a draft schema for Finder B2B CRM

enum Role {
  ADMIN
  MANAGER
  MEMBER
}

enum ActivityType {
  CALL
  MEETING
  EMAIL
  NOTE
}

enum DealStatus {
  LEAD
  MEETING
  PROPOSAL
  CONTRACT
  LOST
}

model User {
  id            String    @id @default(cuid())
  name          String?
  email         String    @unique
  password      String?
  image         String?
  role          Role      @default(MEMBER)
  teamId        String?
  team          Team?     @relation(fields: [teamId], references: [id])
  activities    Activity[]
  deals         Deal[]
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
}

model Team {
  id        String   @id @default(cuid())
  name      String
  users     User[]
  companies Company[]
  createdAt DateTime @default(now())
}

model Company {
  id          String   @id @default(cuid())
  name        String
  industry    String?
  website     String?
  address     String?
  latitude    Float?
  longitude   Float?
  teamId      String?
  team        Team?    @relation(fields: [teamId], references: [id])
  contacts    Contact[]
  deals       Deal[]
  activities  Activity[]
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
}

model Contact {
  id        String   @id @default(cuid())
  name      String
  title     String?
  email     String?
  phone     String?
  companyId String
  company   Company  @relation(fields: [companyId], references: [id])
  deals     Deal[]
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}

model Deal {
  id          String     @id @default(cuid())
  title       String
  value       Float      @default(0)
  status      DealStatus @default(LEAD)
  companyId   String
  company     Company    @relation(fields: [companyId], references: [id])
  contactId   String?
  contact     Contact?   @relation(fields: [contactId], references: [id])
  ownerId     String
  owner       User       @relation(fields: [ownerId], references: [id])
  activities  Activity[]
  createdAt   DateTime   @default(now())
  updatedAt   DateTime   @updatedAt
}

model Activity {
  id          String       @id @default(cuid())
  type        ActivityType @default(NOTE)
  content     String       @db.Text
  userId      String
  user        User         @relation(fields: [userId], references: [id])
  companyId   String?
  company     Company?     @relation(fields: [companyId], references: [id])
  dealId      String?
  deal        Deal?        @relation(fields: [dealId], references: [id])
  attachments Attachment[]
  createdAt   DateTime     @default(now())
}

model Attachment {
  id         String   @id @default(cuid())
  url        String
  filename   String
  activityId String
  activity   Activity @relation(fields: [activityId], references: [id])
  createdAt  DateTime @default(now())
}
```

## 3. 핵심 관계 설명
- **RBAC:** `User.role`과 `User.teamId`를 통해 데이터 접근 권한을 관리합니다.
- **Pipeline:** `Deal.status`를 통해 칸반 보드의 위치를 관리하며, `Activity`와 연동되어 타임라인을 구성합니다.
- **Map:** `Company` 테이블의 `latitude`, `longitude`를 사용하여 Google Maps API에서 마커를 렌더링합니다.
- **OCR:** `Contact` 정보 생성 시 `Attachment`의 이미지를 OCR로 분석하여 `Contact.name`, `Contact.phone` 등을 자동 채웁니다.
