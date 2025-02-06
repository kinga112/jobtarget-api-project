<script setup lang="ts">

  import type { PostingType } from '../types/posting';

  defineProps<{ posting: PostingType }>()

</script>

<template>
  <div class="flex flex-col gap-2 bg-zinc-300 p-5 rounded-md">
    <div>{{ posting.sitename }}</div>
    <div>#{{ posting.id }}</div>
    <div>Duration: {{ posting.duration }}</div>
  </div>
</template>
