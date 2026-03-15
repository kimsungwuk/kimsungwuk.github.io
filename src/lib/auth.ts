import { NextAuthOptions } from "next-auth";
import CredentialsProvider from "next-auth/providers/credentials";
import { Role } from "@prisma/client";

// Mock user with plain text check for stable demo access
const MOCK_USER = {
  id: "admin-id",
  email: "admin@finder.com",
  name: "Admin User",
  password: "admin123",
  role: Role.ADMIN,
};

export const authOptions: NextAuthOptions = {
  session: {
    strategy: "jwt",
  },
  pages: {
    signIn: "/login",
  },
  providers: [
    CredentialsProvider({
      name: "credentials",
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.email || !credentials?.password) return null;

        if (credentials.email === MOCK_USER.email && credentials.password === MOCK_USER.password) {
          return {
            id: MOCK_USER.id,
            email: MOCK_USER.email,
            name: MOCK_USER.name,
            role: MOCK_USER.role,
          } as any;
        }

        return null;
      },
    }),
  ],
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.role = (user as any).role;
        token.id = user.id;
      }
      return token;
    },
    async session({ session, token }) {
      if (session.user) {
        (session.user as any).role = token.role;
        (session.user as any).id = token.id;
      }
      return session;
    },
  },
};
