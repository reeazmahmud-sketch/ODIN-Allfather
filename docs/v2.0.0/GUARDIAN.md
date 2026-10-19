# ODIN — The Allfather v2.0.0
## Guardian

**Date:** 19-10-2026

---

## 1. Evolution from v1

ODIN v1 already monitors disk, memory, and high-CPU processes and sends alerts to enabled agents.

v2 evolves that monitoring loop into the ODIN Guardian: a supervised safety subsystem that observes, diagnoses, contains, recovers, and reports without becoming an unrestricted autonomous administrator.

---

## 2. Guardian Domains

The Guardian monitors:

- CPU utilization and sustained saturation;
- memory pressure and swap pressure;
- disk utilization and free space;
- abnormal disk-growth rate;
- process CPU/memory behavior;
- subprocess trees created by ODIN tasks;
- repeated process crashes;
- stuck or overdue ODIN tasks;
- ODIN daemon health;
- snapshot/log/cache growth.

---

## 3. Detection vs Intervention

Detection does not automatically grant intervention authority.

Response ladder:

```text
OBSERVE
   |
   v
WARN
   |
   v
DIAGNOSE
   |
   v
REQUEST APPROVAL (when required)
   |
   v
CONTAIN
   |
   v
RECOVER
   |
   v
REPORT
```

Low-risk actions may be policy-approved in advance. High-impact actions require explicit authorization.

---

## 4. Runaway Process Detection

A single instantaneous CPU reading is not enough to classify an infinite loop.

Use multiple signals:

- sustained high CPU duration;
- no task progress/heartbeat;
- repeated identical activity;
- process ancestry;
- memory growth;
- disk-write growth;
- task timeout;
- expected workload profile.

Guardian reports confidence and evidence rather than claiming certainty from one threshold.

---

## 5. Disk Growth Protection

Guardian tracks both percentage used and growth velocity.

Examples of triggers:

- free space below configured reserve;
- workspace grows by abnormal amount within a short window;
- one process creates files at abnormal rate;
- logs/snapshots exceed quota.

Possible safe responses:

- warn;
- pause originating ODIN task;
- stop further snapshot creation;
- request approval to terminate an owned subprocess;
- produce a disk-growth report.

Guardian does not delete arbitrary user files to make space.

---

## 6. Process Ownership

Guardian distinguishes:

- ODIN daemon;
- ODIN-owned subprocess;
- agent-owned subprocess launched through ODIN;
- unrelated user/system process.

ODIN may have stronger automatic containment rights over processes it launched itself. External processes require stricter policy.

---

## 7. Emergency Stop

ODIN needs a predictable emergency-stop mechanism that can:

- cancel active ODIN tasks;
- prevent new mutating tasks;
- terminate ODIN-owned child processes according to policy;
- flush durable state;
- preserve audit logs;
- leave workspaces recoverable.

Emergency stop must not be implemented as uncontrolled system-wide process killing.

---

## 8. Guardian Configuration

Configuration should support per-machine thresholds for:

```text
cpu
memory
swap
disk_free
disk_growth
process_duration
task_timeout
snapshot_quota
log_quota
```

Defaults should be conservative and observable before enabling automatic containment.

---

## 9. Reports

Each significant incident should record:

- detection time;
- metric/evidence;
- responsible task/process when known;
- severity;
- action taken;
- authorization used;
- recovery result;
- recommended follow-up.

These records can feed periodic health and chaos-test summaries.

---

## 10. Guardian Invariant

> ODIN protects the machine from ODIN's own agents first; broader system control is explicit, bounded, and auditable.
