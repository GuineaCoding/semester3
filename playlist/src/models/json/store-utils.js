import { JSONFilePreset } from "lowdb/lib/node";

export const db = await JSONFilePreset("src/models/json/db.json", {
  users: [],
  playlists: [],
  tracks: [],
});
