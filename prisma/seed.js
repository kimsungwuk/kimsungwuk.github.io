const { PrismaClient } = require("@prisma/client");
const bcrypt = require("bcryptjs");

const prisma = new PrismaClient();

async function main() {
  // Clear existing data to avoid unique constraint errors during re-seed
  await prisma.attachment.deleteMany();
  await prisma.activity.deleteMany();
  await prisma.deal.deleteMany();
  await prisma.contact.deleteMany();
  await prisma.company.deleteMany();
  await prisma.user.deleteMany();
  await prisma.team.deleteMany();

  const adminPassword = await bcrypt.hash("admin123", 10);
  const managerPassword = await bcrypt.hash("manager123", 10);

  // Create Team
  const team = await prisma.team.create({
    data: {
      name: "Growth Founders",
    },
  });

  // Create Users
  const admin = await prisma.user.create({
    data: {
      name: "Admin User",
      email: "admin@finder.com",
      password: adminPassword,
      role: "ADMIN",
    },
  });

  const manager = await prisma.user.create({
    data: {
      name: "Sales Manager",
      email: "manager@finder.com",
      password: managerPassword,
      role: "MANAGER",
      teamId: team.id,
    },
  });

  // Create Companies
  const acme = await prisma.company.create({
    data: {
      name: "Acme Dynamics",
      industry: "Robotics",
      website: "https://acme-dynamics.com",
      address: "123 Innovation Way, Neo Tokyo",
      latitude: 35.6895,
      longitude: 139.6917,
      teamId: team.id,
    },
  });

  const globalTech = await prisma.company.create({
    data: {
      name: "Global Tech Systems",
      industry: "Software",
      website: "https://globaltech.ai",
      address: "456 Silicon Ave, Mountain View, CA",
      latitude: 37.4221,
      longitude: -122.0841,
      teamId: team.id,
    },
  });

  // Create Contacts
  const contact1 = await prisma.contact.create({
    data: {
      name: "Sarah Connor",
      title: "CTO",
      email: "sarah@acme.com",
      phone: "+1-555-0199",
      companyId: acme.id,
    },
  });

  // Create Deals
  await prisma.deal.createMany({
    data: [
      {
        title: "AI Integration Project",
        value: 125000,
        status: "PROPOSAL",
        companyId: acme.id,
        contactId: contact1.id,
        ownerId: admin.id,
      },
      {
        title: "Cloud Infrastructure Setup",
        value: 45000,
        status: "MEETING",
        companyId: globalTech.id,
        ownerId: manager.id,
      },
      {
        title: "Security Audit",
        value: 15000,
        status: "LEAD",
        companyId: acme.id,
        ownerId: admin.id,
      }
    ],
  });

  console.log("Seeding completed with realistic sample data!");
}

main()
  .catch((e) => {
    console.error(e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
