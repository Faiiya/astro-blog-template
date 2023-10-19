import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";
import tailwind from "@astrojs/tailwind";
import { rehypeHeadingIds } from "@astrojs/markdown-remark";
import vercel from "@astrojs/vercel/serverless";

// https://astro.build/config
export default defineConfig({
  output: "server",
  adapter: vercel(),
  site: "https://comprar.elitewebs.es",
  integrations: [
    mdx({
      optimize: true,
    }),
    sitemap({
      entryLimit: 2000,
    }),
    tailwind(),
  ],
  markdown: {
    rehypePlugins: [rehypeHeadingIds],
  },
});
