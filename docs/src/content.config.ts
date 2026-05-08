import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// Workshop content lives outside the Astro project root in `../workshop-content`.
// Files prefixed with `_` (and anything in `_partials/`) are excluded from routing
// and used as MDX partials imported by other pages.
//
// Starlight's `docsLoader()` hard-codes `src/content/docs` as its base, so we use
// Astro's underlying `glob()` loader directly with `docsSchema()` for the schema.
// Starlight's remark plugins (asides, code blocks, heading anchors) are registered
// at the integration level and apply to all `.md`/`.mdx` content regardless of loader.
export const collections = {
  docs: defineCollection({
    loader: glob({
      base: '../workshop-content',
      pattern: ['**/*.{md,mdx}', '!**/_*/**', '!**/_*', '!node_modules/**'],
    }),
    schema: docsSchema(),
  }),
};
