<script setup lang="ts">

  import { ref } from 'vue';
  import type { JobType } from '../types/job';

  const props = defineProps<{ job: JobType }>()

  const statusColor = ref('text-green-500')
  if(props.job.status == 'Inactive'){
    statusColor.value = 'text-red-500'
  }

  const jobStyle = `
    flex flex-col bg-gray-100 p-5 rounded-xl text-left 
    cursor-pointer text-black hover:bg-zinc-300 border-2 border-gray-300`

</script>

<template>
  <router-link :to="{ name: 'job', params: { id: job.id } }" :class="jobStyle">
    <div class="space-x-3 inline-block align-baseline">
      <span class="text-3xl">{{ job.req_name }}</span>
      <span :class="'font-semibold ' + statusColor">{{ job.status }}</span>
    </div>
    <div class="text-sm">
      {{ job.location.city }}, {{ job.location.state }}, {{ job.location.country }}
    </div>
    <div class="h-3"/> <!-- spacer -->
    <p class="text-lg line-clamp-2">
      {{ job.description }}
    </p>
  </router-link>
</template>
