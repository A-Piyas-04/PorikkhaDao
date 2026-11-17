import path from "node:path";

/** Absolute path to the Phase 0 SQLite bank shared with content tools. */
export function getDbPath() {
  return path.join(process.cwd(), "..", "content", "db", "porikkhadao.sqlite");
}
