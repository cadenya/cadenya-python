# Cadenya Python SDK reference

Keyword arguments are snake_case (nested request dicts too); see README.md for usage patterns.

## client.accounts

Retrieves the current account for the token accessing the API

```python
client.accounts.retrieve() -> Account
```
Rotates the challenge token for the account

```python
client.accounts.rotate_challenge_token() -> RotateChallengeTokenResponse
```
Rotates the webhook signing key for the account

```python
client.accounts.rotate_webhook_signing_key() -> RotateWebhookEventsHmacSecretResponse
```

## client.api_keys

Get the global API key

```python
client.api_keys.retrieve_global() -> APIKey
```
Disable the global API key

```python
client.api_keys.disable_global() -> APIKey
```
Enable the global API key

```python
client.api_keys.enable_global() -> APIKey
```
Rotate the global API key

```python
client.api_keys.rotate_global() -> APIKey
```
List API keys

```python
client.api_keys.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, labels=None, sort_order=None, include_info=None) -> SyncPage[APIKey]
```
Create a new API key

```python
client.api_keys.create(*, workspace_id=None, metadata, spec) -> APIKey
```
Get an API key by ID

```python
client.api_keys.retrieve(id: str, *, workspace_id=None) -> APIKey
```
Delete an API key

```python
client.api_keys.delete(id: str, *, workspace_id=None) -> None
```
Update an API key

```python
client.api_keys.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> APIKey
```
Disable an API key

```python
client.api_keys.disable(id: str, *, workspace_id=None) -> APIKey
```
Enable an API key

```python
client.api_keys.enable(id: str, *, workspace_id=None) -> APIKey
```
Rotate an API key

```python
client.api_keys.rotate(id: str, *, workspace_id=None) -> APIKey
```

## client.workspace_admin

Search account profiles

```python
client.workspace_admin.list_profiles(*, limit=None, cursor=None, query=None, labels=None) -> SyncPage[Profile]
```
List all workspaces in the account

```python
client.workspace_admin.list_account(*, limit=None, cursor=None, include_archived=None, labels=None) -> SyncPage[Workspace]
```
Create a workspace

```python
client.workspace_admin.create(*, metadata, spec) -> Workspace
```
Get a workspace by ID

```python
client.workspace_admin.retrieve(*, workspace_id=None) -> Workspace
```
Archive a workspace

```python
client.workspace_admin.archive(*, workspace_id=None) -> None
```
Update a workspace

```python
client.workspace_admin.update(*, workspace_id=None, metadata=None, spec=None, update_mask=None) -> Workspace
```
List workspace members

```python
client.workspace_admin.list_members(*, workspace_id=None, limit=None, cursor=None) -> SyncPage[WorkspaceMember]
```
Add a member to a workspace

```python
client.workspace_admin.add_member(*, workspace_id=None, profile_id=None, email=None) -> WorkspaceMember
```
Remove a member from a workspace

```python
client.workspace_admin.remove_member(profile_id: str, *, workspace_id=None) -> None
```

## client.profiles

Retrieves the profile for the credentials accessing the API

```python
client.profiles.whoami() -> Profile
```

## client.workspaces

List workspaces

```python
client.workspaces.list(*, limit=None, cursor=None, sort_order=None, include_info=None, labels=None) -> SyncPage[Workspace]
```

## client.agents

List agents

```python
client.agents.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, state=None, variation_selection_mode=None, labels=None, sort_order=None, include_info=None) -> SyncPage[Agent]
```
Create a new agent

```python
client.agents.create(*, workspace_id=None, metadata, spec, default_variation=None) -> Agent
```
List feedback for an agent

```python
client.agents.list_feedback(agent_id: str, *, workspace_id=None, limit=None, cursor=None, query=None, sentiment=None, agent_variation_id=None, created_after=None, created_before=None, labels=None, include_info=None) -> SyncPage[ObjectiveFeedback]
```
List webhook deliveries

```python
client.agents.list_webhook_deliveries(agent_id: str, *, workspace_id=None, cursor=None, limit=None, objective_id=None, event_type=None, labels=None) -> SyncPage[WebhookDelivery]
```
Get an agent by ID

```python
client.agents.retrieve(id: str, *, workspace_id=None) -> Agent
```
Delete an agent

```python
client.agents.delete(id: str, *, workspace_id=None) -> None
```
Update an agent

```python
client.agents.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> Agent
```
Archive an agent

```python
client.agents.archive(id: str, *, workspace_id=None) -> Agent
```
Publish an agent

```python
client.agents.publish(id: str, *, workspace_id=None) -> Agent
```
Unarchive an agent

```python
client.agents.unarchive(id: str, *, workspace_id=None) -> Agent
```
Unpublish an agent

```python
client.agents.unpublish(id: str, *, workspace_id=None) -> Agent
```

## client.agents.schedules

List schedules

```python
client.agents.schedules.list(agent_id: str, *, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, labels=None, sort_order=None, include_info=None) -> SyncPage[AgentSchedule]
```
Create a new schedule

```python
client.agents.schedules.create(agent_id: str, *, workspace_id=None, metadata, spec) -> AgentSchedule
```
Get a schedule by ID

```python
client.agents.schedules.retrieve(agent_id: str, id: str, *, workspace_id=None) -> AgentSchedule
```
Delete a schedule

```python
client.agents.schedules.delete(agent_id: str, id: str, *, workspace_id=None) -> None
```
Update a schedule

```python
client.agents.schedules.update(agent_id: str, id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> AgentSchedule
```
Archive a schedule

```python
client.agents.schedules.archive(agent_id: str, id: str, *, workspace_id=None) -> AgentSchedule
```
Pause a schedule

```python
client.agents.schedules.pause(agent_id: str, id: str, *, workspace_id=None) -> AgentSchedule
```
Resume a schedule

```python
client.agents.schedules.resume(agent_id: str, id: str, *, workspace_id=None) -> AgentSchedule
```

## client.agents.variations

List variations

```python
client.agents.variations.list(agent_id: str, *, workspace_id=None, limit=None, cursor=None, sort_order=None, include_info=None, labels=None) -> SyncPage[AgentVariation]
```
Create a new variation

```python
client.agents.variations.create(agent_id: str, *, workspace_id=None, metadata, spec) -> AgentVariation
```
Get a variation by ID

```python
client.agents.variations.retrieve(agent_id: str, id: str, *, workspace_id=None) -> AgentVariation
```
Delete a variation

```python
client.agents.variations.delete(agent_id: str, id: str, *, workspace_id=None) -> None
```
Update a variation

```python
client.agents.variations.update(agent_id: str, id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> AgentVariation
```
Add an assignment to a variation

```python
client.agents.variations.add_assignment(agent_id: str, variation_id: str, *, workspace_id=None, body) -> VariationAssignment
```
Remove an assignment from a variation

```python
client.agents.variations.remove_assignment(agent_id: str, variation_id: str, id: str, *, workspace_id=None) -> None
```
Attach a memory layer to a variation

```python
client.agents.variations.add_memory_layer(agent_id: str, variation_id: str, *, workspace_id=None, memory_layer_id, position=None) -> VariationMemoryLayerAssignment
```
Remove a memory layer assignment from a variation

```python
client.agents.variations.remove_memory_layer(agent_id: str, variation_id: str, id: str, *, workspace_id=None) -> None
```
Update a variation's memory layer assignment

```python
client.agents.variations.update_memory_layer(agent_id: str, variation_id: str, id: str, *, workspace_id=None, position=None) -> VariationMemoryLayerAssignment
```

## client.ai_provider_keys

List AI provider keys

```python
client.ai_provider_keys.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, promotional=None, labels=None, sort_order=None, include_info=None) -> SyncPage[AIProviderKey]
```
Create a new AI provider key

```python
client.ai_provider_keys.create(*, workspace_id=None, metadata, spec) -> AIProviderKey
```
Get an AI provider key by ID

```python
client.ai_provider_keys.retrieve(id: str, *, workspace_id=None) -> AIProviderKey
```
Delete an AI provider key

```python
client.ai_provider_keys.delete(id: str, *, workspace_id=None) -> None
```
Update an AI provider key

```python
client.ai_provider_keys.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> AIProviderKey
```

## client.memory_layers

List memory layers

```python
client.memory_layers.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, type=None, agent_id=None, episodic_key_prefix=None, labels=None, sort_order=None, include_info=None) -> SyncPage[MemoryLayer]
```
Create a new memory layer

```python
client.memory_layers.create(*, workspace_id=None, metadata, spec) -> MemoryLayer
```
Get a memory layer by ID

```python
client.memory_layers.retrieve(id: str, *, workspace_id=None) -> MemoryLayer
```
Delete a memory layer

```python
client.memory_layers.delete(id: str, *, workspace_id=None) -> None
```
Update a memory layer

```python
client.memory_layers.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> MemoryLayer
```

## client.memory_layers.entries

List memory entries

```python
client.memory_layers.entries.list(memory_layer_id: str, *, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, labels=None, sort_order=None, include_info=None) -> SyncPage[MemoryEntry]
```
Create a new memory entry

```python
client.memory_layers.entries.create(memory_layer_id: str, *, workspace_id=None, metadata, spec) -> MemoryEntryDetail
```
Get a memory entry by ID

```python
client.memory_layers.entries.retrieve(memory_layer_id: str, id: str, *, workspace_id=None) -> MemoryEntryDetail
```
Delete a memory entry

```python
client.memory_layers.entries.delete(memory_layer_id: str, id: str, *, workspace_id=None) -> None
```
Update a memory entry

```python
client.memory_layers.entries.update(memory_layer_id: str, id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> MemoryEntryDetail
```

## client.models

List models

```python
client.models.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, state=None, ai_provider_key_id=None, is_assigned=None, labels=None, sort_order=None, include_info=None) -> SyncPage[Model]
```
Get a model by ID

```python
client.models.retrieve(id: str, *, workspace_id=None) -> Model
```
Disable a model

```python
client.models.disable(id: str, *, workspace_id=None) -> Model
```
Enable a model

```python
client.models.enable(id: str, *, workspace_id=None) -> Model
```
Swap models on agent variations

```python
client.models.swap_on_variations(*, workspace_id=None, model_swaps=None) -> None
```

## client.objectives

List objectives

```python
client.objectives.list(*, workspace_id=None, limit=None, cursor=None, agent_id=None, parent_objective_id=None, state=None, profile_id=None, sort_order=None, include_info=None, agent_schedule_id=None, labels=None, tenant_id=None, subject_id=None, widget_id=None, widget_session_id=None) -> SyncPage[Objective]
```
Create a new objective

```python
client.objectives.create(*, workspace_id=None, agent_id, variation_id=None, metadata=None, system_prompt_data, first_user_message=None, secrets=None, memory_cascade=None, first_user_message_data=None, episodic_memory=None, tenant=None, subject=None, pinned_parameters=None) -> Objective
```
Get an objective by ID

```python
client.objectives.retrieve(id: str, *, workspace_id=None) -> Objective
```
List objective context windows

```python
client.objectives.list_context_windows(objective_id: str, *, workspace_id=None, limit=None, cursor=None, include_info=None, labels=None) -> SyncPage[ObjectiveContextWindow]
```
Get objective context usage

```python
client.objectives.retrieve_diagnostics(objective_id: str, *, workspace_id=None) -> GetObjectiveDiagnosticsResponse
```
List objective events

```python
client.objectives.list_events(objective_id: str, *, workspace_id=None, limit=None, cursor=None, sort_order=None, include_info=None, window_id=None, since_event_id=None, labels=None) -> SyncPage[ObjectiveEvent]
```
Stream objective events

```python
client.objectives.stream_events(objective_id: str, *, workspace_id=None, last_event_id=None) -> Stream[ObjectiveEvent]
```
List feedback for an objective

```python
client.objectives.list_feedback(objective_id: str, *, workspace_id=None, limit=None, cursor=None, labels=None) -> SyncPage[ObjectiveFeedback]
```
Submit feedback for an objective

```python
client.objectives.create_feedback(objective_id: str, *, workspace_id=None, metadata, data) -> ObjectiveFeedback
```
List objective tasks

```python
client.objectives.list_tasks(objective_id: str, *, workspace_id=None, limit=None, cursor=None, sort_order=None) -> SyncPage[ObjectiveTask]
```
Get an objective task by ID

```python
client.objectives.retrieve_task(objective_id: str, id: str, *, workspace_id=None) -> ObjectiveTask
```
List objective tool calls

```python
client.objectives.list_tool_calls(objective_id: str, *, workspace_id=None, limit=None, cursor=None, status=None, include_info=None, execution_status=None, labels=None) -> SyncPage[ObjectiveToolCall]
```
Get an objective tool call by ID

```python
client.objectives.retrieve_tool_call(objective_id: str, tool_call_id: str, *, workspace_id=None) -> ObjectiveToolCallWithResult
```
Approve a tool call

```python
client.objectives.approve_tool_call(objective_id: str, tool_call_id: str, *, workspace_id=None) -> ObjectiveToolCall
```
Deny a tool call

```python
client.objectives.deny_tool_call(objective_id: str, tool_call_id: str, *, workspace_id=None, memo=None) -> ObjectiveToolCall
```
Set a bare tool call's content

```python
client.objectives.set_tool_call_content(objective_id: str, tool_call_id: str, *, workspace_id=None, content) -> ObjectiveToolCall
```
List objective tools

```python
client.objectives.list_tools(objective_id: str, *, workspace_id=None, limit=None, cursor=None) -> SyncPage[ObjectiveTool]
```
Cancel an objective

```python
client.objectives.cancel(objective_id: str, *, workspace_id=None, reason=None) -> Objective
```
Compact an objective

```python
client.objectives.compact(objective_id: str, *, workspace_id=None, compaction_config=None) -> CompactObjectiveResponse
```
Continue an objective

```python
client.objectives.continue_(objective_id: str, *, workspace_id=None, message, enqueue=None) -> ObjectiveEvent
```

## client.tool_search

Search for tools or tool sets

```python
client.tool_search.search_or_sets(*, workspace_id=None, query) -> SearchToolsOrToolSetsResponse
```

## client.tenants

List tenants

```python
client.tenants.list(*, workspace_id=None, limit=None, cursor=None, query=None, labels=None, sort_order=None, include_info=None) -> SyncPage[Tenant]
```
Get a tenant by ID

```python
client.tenants.retrieve(id: str, *, workspace_id=None, include_info=None) -> Tenant
```
Erase a tenant

```python
client.tenants.delete(id: str, *, workspace_id=None) -> Tenant
```
List a tenant's subjects

```python
client.tenants.list_subjects(tenant_id: str, *, workspace_id=None, limit=None, cursor=None, query=None, sort_order=None, include_info=None) -> SyncPage[Subject]
```

## client.tool_sets

List tool sets

```python
client.tool_sets.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, state=None, labels=None, sort_order=None, include_info=None) -> SyncPage[ToolSet]
```
Create a new tool set

```python
client.tool_sets.create(*, workspace_id=None, metadata, spec) -> ToolSet
```
Get a tool set by ID

```python
client.tool_sets.retrieve(id: str, *, workspace_id=None) -> ToolSet
```
Delete a tool set

```python
client.tool_sets.delete(id: str, *, workspace_id=None) -> None
```
Update a tool set

```python
client.tool_sets.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> ToolSet
```
Archive a tool set

```python
client.tool_sets.archive(id: str, *, workspace_id=None) -> ToolSet
```
Unarchive a tool set

```python
client.tool_sets.unarchive(id: str, *, workspace_id=None) -> ToolSet
```
List tool set events

```python
client.tool_sets.list_events(tool_set_id: str, *, workspace_id=None, limit=None, cursor=None, sort_order=None, include_info=None, labels=None) -> SyncPage[ToolSetEvent]
```
Get consumed OpenAPI spec

```python
client.tool_sets.retrieve_open_api_spec(tool_set_id: str, *, workspace_id=None) -> GetToolSetOpenAPISpecResponse
```
List tool set usage

```python
client.tool_sets.list_usage(tool_set_id: str, *, workspace_id=None, tool_id=None, limit=None, cursor=None, sort_order=None) -> SyncPage[ToolSetUsage]
```

## client.tool_sets.secrets

List tool set secrets

```python
client.tool_sets.secrets.list(tool_set_id: str, *, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, sort_order=None, include_info=None) -> SyncPage[ToolSetSecret]
```
Create a new tool set secret

```python
client.tool_sets.secrets.create(tool_set_id: str, *, workspace_id=None, metadata, spec) -> ToolSetSecret
```
Get a tool set secret by ID

```python
client.tool_sets.secrets.retrieve(tool_set_id: str, id: str, *, workspace_id=None) -> ToolSetSecret
```
Delete a tool set secret

```python
client.tool_sets.secrets.delete(tool_set_id: str, id: str, *, workspace_id=None) -> None
```
Update a tool set secret

```python
client.tool_sets.secrets.update(tool_set_id: str, id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> ToolSetSecret
```

## client.tool_sets.tools

List tools

```python
client.tool_sets.tools.list(tool_set_id: str, *, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, names=None, states=None, requires_approval=None, overlays=None, labels=None, sort_order=None, include_info=None) -> SyncPage[Tool]
```
Create a new tool

```python
client.tool_sets.tools.create(tool_set_id: str, *, workspace_id=None, metadata, spec) -> Tool
```
Get a tool by ID

```python
client.tool_sets.tools.retrieve(tool_set_id: str, id: str, *, workspace_id=None) -> Tool
```
Delete a tool

```python
client.tool_sets.tools.delete(tool_set_id: str, id: str, *, workspace_id=None) -> None
```
Update a tool

```python
client.tool_sets.tools.update(tool_set_id: str, id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> Tool
```
Omit a tool

```python
client.tool_sets.tools.omit(tool_set_id: str, id: str, *, workspace_id=None) -> Tool
```
Restore a tool

```python
client.tool_sets.tools.restore(tool_set_id: str, id: str, *, workspace_id=None) -> Tool
```

## client.uploads

Create an upload

```python
client.uploads.create(*, workspace_id=None, metadata, spec) -> Upload
```
Get an upload by ID

```python
client.uploads.retrieve(id: str, *, workspace_id=None) -> Upload
```

## client.widget_sessions

List widget sessions

```python
client.widget_sessions.list(*, workspace_id=None, limit=None, cursor=None, widget_id=None, tenant_id=None, subject_id=None, state=None, labels=None, sort_order=None, include_info=None) -> SyncPage[WidgetSession]
```
Create a widget session

```python
client.widget_sessions.create(*, workspace_id=None, metadata=None, spec, secrets=None) -> WidgetSession
```
Delete all of a tenant's widget sessions

```python
client.widget_sessions.delete_tenant(*, workspace_id=None, tenant_id=None) -> DeleteTenantWidgetSessionsResponse
```
Get a widget session by ID

```python
client.widget_sessions.retrieve(id: str, *, workspace_id=None) -> WidgetSession
```
Delete a widget session

```python
client.widget_sessions.delete(id: str, *, workspace_id=None) -> None
```
Revoke a widget session

```python
client.widget_sessions.revoke(id: str, *, workspace_id=None) -> WidgetSession
```

## client.widgets

List widgets

```python
client.widgets.list(*, workspace_id=None, limit=None, cursor=None, agent_id=None, labels=None, sort_order=None, include_info=None) -> SyncPage[Widget]
```
Create a new widget

```python
client.widgets.create(*, workspace_id=None, metadata, spec) -> Widget
```
Get a widget by ID

```python
client.widgets.retrieve(id: str, *, workspace_id=None) -> Widget
```
Delete a widget

```python
client.widgets.delete(id: str, *, workspace_id=None) -> None
```
Update a widget

```python
client.widgets.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> Widget
```
Archive a widget

```python
client.widgets.archive(id: str, *, workspace_id=None) -> Widget
```
Unarchive a widget

```python
client.widgets.unarchive(id: str, *, workspace_id=None) -> Widget
```

## client.workspace_secrets

List workspace secrets

```python
client.workspace_secrets.list(*, workspace_id=None, limit=None, cursor=None, prefix=None, query=None, labels=None, sort_order=None, include_info=None) -> SyncPage[WorkspaceSecret]
```
Create a new workspace secret

```python
client.workspace_secrets.create(*, workspace_id=None, metadata, spec) -> WorkspaceSecret
```
Get a workspace secret by ID

```python
client.workspace_secrets.retrieve(id: str, *, workspace_id=None) -> WorkspaceSecret
```
Delete a workspace secret

```python
client.workspace_secrets.delete(id: str, *, workspace_id=None) -> None
```
Update a workspace secret

```python
client.workspace_secrets.update(id: str, *, workspace_id=None, metadata=None, spec=None, update_mask=None) -> WorkspaceSecret
```
