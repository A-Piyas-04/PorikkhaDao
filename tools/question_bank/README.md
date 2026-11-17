# PorikkhaDao question-bank tools (Phase 0)

Local SQLite bank + CSV import. No Supabase until after Phase 3.

## Commands

Run from this directory:

```bash
python cli.py init-db
python cli.py seed-syllabus
python cli.py write-template
python generate_pilot.py
python cli.py validate --csv ../../content/pilot/physics_2nd_ch1_ch2.csv
python cli.py import --csv ../../content/pilot/physics_2nd_ch1_ch2.csv
python cli.py stats
python cli.py count --topics "phy2_ch01_t01;phy2_ch01_t02;phy2_ch01_t03"
```

Eligible count uses a **strict** topic filter: every topic tag on a question must be in the include list. Only `verified=1` rows count by default.
