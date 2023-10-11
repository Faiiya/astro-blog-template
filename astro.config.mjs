import { defineConfig } from "astro/config";
import mdx from "@astrojs/mdx";
import sitemap from "@astrojs/sitemap";

import tailwind from "@astrojs/tailwind";
import { rehypeHeadingIds } from "@astrojs/markdown-remark";
// https://astro.build/config
export default defineConfig({
  site: "https://example.com",
  integrations: [
    mdx({
      optimize: { customComponentNames: ["Cta", "CtaBot", "GifSeo", "Gmaps", "Video"] },
    }),
    sitemap(),
    tailwind(),
  ],
  markdown: {
    rehypePlugins: [rehypeHeadingIds],
  },
});
