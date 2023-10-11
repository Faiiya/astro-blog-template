import { defineCollection, z } from "astro:content";

const blog = defineCollection({
  // Type-check frontmatter using a schema
  schema: z.object({
    title: z.string(),
    summary: z.string().nullable().default("") ,
    date: z.coerce.date().optional(),
    banner: z.string(),
    fondoBanner: z.string(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
  }),
});

export const collections = { blog };
