import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

// We use Astro's `glob()` loader directly (instead of Starlight's `docsLoader()`)
// so we can exclude underscore-prefixed *directories* like `_images/`. Starlight's
// default loader only excludes underscore-prefixed *filenames*. Without this exclude,
// assets under `_images/` could be picked up by the content collection.
//
// Starlight's remark plugins (asides, code blocks, heading anchors) are registered
// at the integration level and apply to all `.md`/`.mdx` content regardless of loader.
export const collections = {
  docs: defineCollection({
    loader: glob({
      base: 'src/content/docs',
      pattern: ['**/*.{md,mdx}', '!**/_*/**', '!**/_*'],
    }),
    schema: docsSchema(),
  }),
};
