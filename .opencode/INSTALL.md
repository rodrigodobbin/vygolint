# Installing vygolint for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed

## Installation

Add vygolint to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["vygolint@git+https://github.com/rodrigodobbin/vygolint.git"]
}
```

Restart OpenCode. The plugin installs through OpenCode's plugin manager and
registers all skills.

Verify by asking: "Tell me about your vygolint skills"

OpenCode uses its own plugin install. If you also use Claude Code, Codex, or
another harness, install vygolint separately for each one.

## Usage

Use OpenCode's native `skill` tool:

```
use skill tool to list skills
use skill tool to load vygolint-avaliar
```

## Updating

OpenCode installs vygolint through a git-backed package spec. Some OpenCode
and Bun versions pin that resolved git dependency in a lockfile or cache, so a
restart may not pick up the newest commit. If updates do not appear,
clear OpenCode's package cache or reinstall the plugin.

To pin a specific version:

```json
{
  "plugin": ["vygolint@git+https://github.com/rodrigodobbin/vygolint.git#v0.2.0"]
}
```
