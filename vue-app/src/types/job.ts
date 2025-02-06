import type { PostingType } from "./posting";

export type JobType = {
  postings: Array<PostingType>
  id: number;
  req_name: string;
  location: { city: string, state: string, country: string };
  description: string;
  status: string
}
