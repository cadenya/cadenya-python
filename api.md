# Shared Types

```python
from cadenya.types import (
    AccountResourceMetadata,
    BareMetadata,
    CreateOperationMetadata,
    CreateResourceMetadata,
    OperationMetadata,
    ResourceMetadata,
    UpdateResourceMetadata,
)
```

# AIProviderKeys

Types:

```python
from cadenya.types import (
    AIProviderConfigOpenAI,
    AIProviderConfigOpenAICompatible,
    AIProviderConfigOpenrouter,
    AIProviderCredentialAPIKey,
    AIProviderCredentialHeaders,
    AIProviderKey,
    AIProviderKeySpec,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/ai_provider_keys">client.ai_provider_keys.<a href="./src/cadenya/resources/ai_provider_keys.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/ai_provider_key_create_params.py">params</a>) -> <a href="./src/cadenya/types/ai_provider_key.py">AIProviderKey</a></code>
- <code title="get /v1/workspaces/{workspaceId}/ai_provider_keys/{id}">client.ai_provider_keys.<a href="./src/cadenya/resources/ai_provider_keys.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/ai_provider_key.py">AIProviderKey</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/ai_provider_keys/{id}">client.ai_provider_keys.<a href="./src/cadenya/resources/ai_provider_keys.py">update</a>(id, \*, workspace_id, \*\*<a href="src/cadenya/types/ai_provider_key_update_params.py">params</a>) -> <a href="./src/cadenya/types/ai_provider_key.py">AIProviderKey</a></code>
- <code title="get /v1/workspaces/{workspaceId}/ai_provider_keys">client.ai_provider_keys.<a href="./src/cadenya/resources/ai_provider_keys.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/ai_provider_key_list_params.py">params</a>) -> <a href="./src/cadenya/types/ai_provider_key.py">SyncCursorPagination[AIProviderKey]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/ai_provider_keys/{id}">client.ai_provider_keys.<a href="./src/cadenya/resources/ai_provider_keys.py">delete</a>(id, \*, workspace_id) -> None</code>

# Account

Types:

```python
from cadenya.types import (
    Account,
    AccountInfo,
    AccountSpec,
    Profile,
    ProfileSpec,
    RotateChallengeTokenResponse,
    RotateWebhookSigningKeyResponse,
)
```

Methods:

- <code title="get /v1/account">client.account.<a href="./src/cadenya/resources/account.py">retrieve</a>() -> <a href="./src/cadenya/types/account.py">Account</a></code>
- <code title="post /v1/account:rotateChallengeToken">client.account.<a href="./src/cadenya/resources/account.py">rotate_challenge_token</a>() -> <a href="./src/cadenya/types/rotate_challenge_token_response.py">RotateChallengeTokenResponse</a></code>
- <code title="post /v1/account:rotateWebhookSigningKey">client.account.<a href="./src/cadenya/resources/account.py">rotate_webhook_signing_key</a>() -> <a href="./src/cadenya/types/rotate_webhook_signing_key_response.py">RotateWebhookSigningKeyResponse</a></code>

# Profiles

Methods:

- <code title="get /v1/whoami">client.profiles.<a href="./src/cadenya/resources/profiles.py">whoami</a>() -> <a href="./src/cadenya/types/profile.py">Profile</a></code>

# Agents

Types:

```python
from cadenya.types import Agent, AgentInfo, AgentSpec, Page
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/agents">client.agents.<a href="./src/cadenya/resources/agents/agents.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/agent_create_params.py">params</a>) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>
- <code title="get /v1/workspaces/{workspaceId}/agents/{id}">client.agents.<a href="./src/cadenya/resources/agents/agents.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/agents/{id}">client.agents.<a href="./src/cadenya/resources/agents/agents.py">update</a>(id, \*, workspace_id, \*\*<a href="src/cadenya/types/agent_update_params.py">params</a>) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>
- <code title="get /v1/workspaces/{workspaceId}/agents">client.agents.<a href="./src/cadenya/resources/agents/agents.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/agent_list_params.py">params</a>) -> <a href="./src/cadenya/types/agent.py">SyncCursorPagination[Agent]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/agents/{id}">client.agents.<a href="./src/cadenya/resources/agents/agents.py">delete</a>(id, \*, workspace_id) -> None</code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{id}:archive">client.agents.<a href="./src/cadenya/resources/agents/agents.py">archive</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{id}:publish">client.agents.<a href="./src/cadenya/resources/agents/agents.py">publish</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{id}:unarchive">client.agents.<a href="./src/cadenya/resources/agents/agents.py">unarchive</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{id}:unpublish">client.agents.<a href="./src/cadenya/resources/agents/agents.py">unpublish</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/agent.py">Agent</a></code>

## Feedback

Methods:

- <code title="get /v1/workspaces/{workspaceId}/agents/{agentId}/feedback">client.agents.feedback.<a href="./src/cadenya/resources/agents/feedback.py">list</a>(agent_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/feedback_list_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_feedback.py">SyncCursorPagination[ObjectiveFeedback]</a></code>

## WebhookDeliveries

Types:

```python
from cadenya.types.agents import WebhookDelivery, WebhookDeliveryData
```

Methods:

- <code title="get /v1/workspaces/{workspaceId}/agents/{agentId}/webhook_deliveries">client.agents.webhook_deliveries.<a href="./src/cadenya/resources/agents/webhook_deliveries.py">list</a>(agent_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/webhook_delivery_list_params.py">params</a>) -> <a href="./src/cadenya/types/agents/webhook_delivery.py">SyncCursorPagination[WebhookDelivery]</a></code>

## Variations

Types:

```python
from cadenya.types.agents import (
    AddAgentVariationAssignmentRequestSubAgentID,
    AddAgentVariationAssignmentRequestToolID,
    AddAgentVariationAssignmentRequestToolSetID,
    AgentVariation,
    AgentVariationInfo,
    AgentVariationSpec,
    AgentVariationSpecCompactionConfig,
    AgentVariationSpecConstraints,
    AgentVariationSpecModelConfig,
    AgentVariationSpecProgressiveDiscovery,
    CompactionConfigSummarizationStrategy,
    CompactionConfigToolResultClearingStrategy,
    VariationAssignment,
    VariationAssignmentAgent,
    VariationAssignmentTool,
    VariationAssignmentToolSet,
    VariationMemoryLayerAssignment,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/variations">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">create</a>(agent_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/variation_create_params.py">params</a>) -> <a href="./src/cadenya/types/agents/agent_variation.py">AgentVariation</a></code>
- <code title="get /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{id}">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">retrieve</a>(agent_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/agents/agent_variation.py">AgentVariation</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{id}">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">update</a>(agent_id, id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/variation_update_params.py">params</a>) -> <a href="./src/cadenya/types/agents/agent_variation.py">AgentVariation</a></code>
- <code title="get /v1/workspaces/{workspaceId}/agents/{agentId}/variations">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">list</a>(agent_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/variation_list_params.py">params</a>) -> <a href="./src/cadenya/types/agents/agent_variation.py">SyncCursorPagination[AgentVariation]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{id}">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">delete</a>(agent_id, id, \*, workspace_id) -> None</code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{variationId}/assignments">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">add_assignment</a>(agent_id, variation_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/variation_add_assignment_params.py">params</a>) -> <a href="./src/cadenya/types/agents/variation_assignment.py">VariationAssignment</a></code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{variationId}/memory_layer_assignments">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">add_memory_layer</a>(agent_id, variation_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/variation_add_memory_layer_params.py">params</a>) -> <a href="./src/cadenya/types/agents/variation_memory_layer_assignment.py">VariationMemoryLayerAssignment</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{variationId}/assignments/{id}">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">remove_assignment</a>(agent_id, variation_id, id, \*, workspace_id) -> None</code>
- <code title="delete /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{variationId}/memory_layer_assignments/{id}">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">remove_memory_layer</a>(agent_id, variation_id, id, \*, workspace_id) -> None</code>
- <code title="patch /v1/workspaces/{workspaceId}/agents/{agentId}/variations/{variationId}/memory_layer_assignments/{id}">client.agents.variations.<a href="./src/cadenya/resources/agents/variations.py">update_memory_layer</a>(agent_id, variation_id, id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/variation_update_memory_layer_params.py">params</a>) -> <a href="./src/cadenya/types/agents/variation_memory_layer_assignment.py">VariationMemoryLayerAssignment</a></code>

## Schedules

Types:

```python
from cadenya.types.agents import (
    AgentSchedule,
    AgentScheduleInfo,
    AgentScheduleSpec,
    AgentScheduleSpecSchedule,
    ScheduleCalendar,
    ScheduleInterval,
    ScheduleRange,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/schedules">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">create</a>(agent_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/schedule_create_params.py">params</a>) -> <a href="./src/cadenya/types/agents/agent_schedule.py">AgentSchedule</a></code>
- <code title="get /v1/workspaces/{workspaceId}/agents/{agentId}/schedules/{id}">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">retrieve</a>(agent_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/agents/agent_schedule.py">AgentSchedule</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/agents/{agentId}/schedules/{id}">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">update</a>(agent_id, id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/schedule_update_params.py">params</a>) -> <a href="./src/cadenya/types/agents/agent_schedule.py">AgentSchedule</a></code>
- <code title="get /v1/workspaces/{workspaceId}/agents/{agentId}/schedules">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">list</a>(agent_id, \*, workspace_id, \*\*<a href="src/cadenya/types/agents/schedule_list_params.py">params</a>) -> <a href="./src/cadenya/types/agents/agent_schedule.py">SyncCursorPagination[AgentSchedule]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/agents/{agentId}/schedules/{id}">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">delete</a>(agent_id, id, \*, workspace_id) -> None</code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/schedules/{id}:archive">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">archive</a>(agent_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/agents/agent_schedule.py">AgentSchedule</a></code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/schedules/{id}:pause">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">pause</a>(agent_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/agents/agent_schedule.py">AgentSchedule</a></code>
- <code title="post /v1/workspaces/{workspaceId}/agents/{agentId}/schedules/{id}:resume">client.agents.schedules.<a href="./src/cadenya/resources/agents/schedules.py">resume</a>(agent_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/agents/agent_schedule.py">AgentSchedule</a></code>

# Objectives

Types:

```python
from cadenya.types import (
    AssistantMessage,
    AssistantToolCall,
    CallableTool,
    CallableToolAgent,
    CallableToolCadenyaProvidedTool,
    CallableToolTool,
    ContextLengths,
    ContextWindowCompacted,
    MemoryRead,
    MemoryReference,
    Objective,
    ObjectiveConfigSnapshot,
    ObjectiveContextWindow,
    ObjectiveContextWindowData,
    ObjectiveDiagnostics,
    ObjectiveError,
    ObjectiveEvent,
    ObjectiveEventData,
    ObjectiveEventDataAssistantMessage,
    ObjectiveEventDataCancelled,
    ObjectiveEventDataContextWindowCompacted,
    ObjectiveEventDataError,
    ObjectiveEventDataFinalized,
    ObjectiveEventDataMemoryRead,
    ObjectiveEventDataNotice,
    ObjectiveEventDataSubAgentSpawned,
    ObjectiveEventDataSubAgentUpdated,
    ObjectiveEventDataTimedOut,
    ObjectiveEventDataToolApprovalRequested,
    ObjectiveEventDataToolApproved,
    ObjectiveEventDataToolCalled,
    ObjectiveEventDataToolDenied,
    ObjectiveEventDataToolError,
    ObjectiveEventDataToolResult,
    ObjectiveEventDataUserMessage,
    ObjectiveEventInfo,
    ObjectiveEventWebhookData,
    ObjectiveInfo,
    ObjectiveSecret,
    SubAgentSpawned,
    SubAgentUpdated,
    ToolApprovalRequested,
    ToolApproved,
    ToolCalled,
    ToolDenied,
    ToolError,
    ToolResult,
    UserMessage,
    ObjectiveCompactResponse,
    ObjectiveRetrieveDiagnosticsResponse,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/objectives">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/objective_create_params.py">params</a>) -> <a href="./src/cadenya/types/objective.py">Objective</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{id}">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/objective.py">Objective</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/objective_list_params.py">params</a>) -> <a href="./src/cadenya/types/objective.py">SyncCursorPagination[Objective]</a></code>
- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}:cancel">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">cancel</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objective_cancel_params.py">params</a>) -> <a href="./src/cadenya/types/objective.py">Objective</a></code>
- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}:compact">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">compact</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objective_compact_params.py">params</a>) -> <a href="./src/cadenya/types/objective_compact_response.py">ObjectiveCompactResponse</a></code>
- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}:continue">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">continue\_</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objective_continue_params.py">params</a>) -> <a href="./src/cadenya/types/objective_event.py">ObjectiveEvent</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/context_windows">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">list_context_windows</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objective_list_context_windows_params.py">params</a>) -> <a href="./src/cadenya/types/objective_context_window.py">SyncCursorPagination[ObjectiveContextWindow]</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/events">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">list_events</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objective_list_events_params.py">params</a>) -> <a href="./src/cadenya/types/objective_event.py">SyncCursorPagination[ObjectiveEvent]</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/diagnostics">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">retrieve_diagnostics</a>(objective_id, \*, workspace_id) -> <a href="./src/cadenya/types/objective_retrieve_diagnostics_response.py">ObjectiveRetrieveDiagnosticsResponse</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/events:stream">client.objectives.<a href="./src/cadenya/resources/objectives/objectives.py">stream_events</a>(objective_id, \*, workspace_id) -> <a href="./src/cadenya/types/objective_event.py">ObjectiveEvent</a></code>

## Tools

Types:

```python
from cadenya.types.objectives import ObjectiveTool
```

Methods:

- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tools">client.objectives.tools.<a href="./src/cadenya/resources/objectives/tools.py">list</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/tool_list_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_tool.py">SyncCursorPagination[ObjectiveTool]</a></code>

## ToolCalls

Types:

```python
from cadenya.types.objectives import (
    ObjectiveToolCall,
    ObjectiveToolCallData,
    ObjectiveToolCallInfo,
    ObjectiveToolCallResult,
    ObjectiveToolCallResultAudioBlock,
    ObjectiveToolCallResultContentBlock,
    ObjectiveToolCallResultContentBlockAudio,
    ObjectiveToolCallResultContentBlockImage,
    ObjectiveToolCallResultContentBlockText,
    ObjectiveToolCallResultImageBlock,
    ObjectiveToolCallResultTextBlock,
    ObjectiveToolCallWithResult,
    ResolvedSecret,
    SetToolCallContentRequestAudioBlock,
    SetToolCallContentRequestContentBlock,
    SetToolCallContentRequestContentBlockAudio,
    SetToolCallContentRequestContentBlockImage,
    SetToolCallContentRequestContentBlockText,
    SetToolCallContentRequestImageBlock,
    SetToolCallContentRequestTextBlock,
)
```

Methods:

- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tool_calls/{toolCallId}">client.objectives.tool_calls.<a href="./src/cadenya/resources/objectives/tool_calls.py">retrieve</a>(objective_id, tool_call_id, \*, workspace_id) -> <a href="./src/cadenya/types/objectives/objective_tool_call_with_result.py">ObjectiveToolCallWithResult</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tool_calls">client.objectives.tool_calls.<a href="./src/cadenya/resources/objectives/tool_calls.py">list</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/tool_call_list_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_tool_call.py">SyncCursorPagination[ObjectiveToolCall]</a></code>
- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tool_calls/{toolCallId}:approve">client.objectives.tool_calls.<a href="./src/cadenya/resources/objectives/tool_calls.py">approve</a>(objective_id, tool_call_id, \*, workspace_id) -> <a href="./src/cadenya/types/objectives/objective_tool_call.py">ObjectiveToolCall</a></code>
- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tool_calls/{toolCallId}:deny">client.objectives.tool_calls.<a href="./src/cadenya/resources/objectives/tool_calls.py">deny</a>(objective_id, tool_call_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/tool_call_deny_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_tool_call.py">ObjectiveToolCall</a></code>
- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tool_calls/{toolCallId}:setContent">client.objectives.tool_calls.<a href="./src/cadenya/resources/objectives/tool_calls.py">set_content</a>(objective_id, tool_call_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/tool_call_set_content_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_tool_call.py">ObjectiveToolCall</a></code>

## Tasks

Types:

```python
from cadenya.types.objectives import ObjectiveTask, ObjectiveTaskData
```

Methods:

- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tasks/{id}">client.objectives.tasks.<a href="./src/cadenya/resources/objectives/tasks.py">retrieve</a>(objective_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/objectives/objective_task.py">ObjectiveTask</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/tasks">client.objectives.tasks.<a href="./src/cadenya/resources/objectives/tasks.py">list</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/task_list_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_task.py">SyncCursorPagination[ObjectiveTask]</a></code>

## Feedback

Types:

```python
from cadenya.types.objectives import ObjectiveFeedback, ObjectiveFeedbackData, ObjectiveFeedbackInfo
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/objectives/{objectiveId}/feedback">client.objectives.feedback.<a href="./src/cadenya/resources/objectives/feedback.py">create</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/feedback_create_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_feedback.py">ObjectiveFeedback</a></code>
- <code title="get /v1/workspaces/{workspaceId}/objectives/{objectiveId}/feedback">client.objectives.feedback.<a href="./src/cadenya/resources/objectives/feedback.py">list</a>(objective_id, \*, workspace_id, \*\*<a href="src/cadenya/types/objectives/feedback_list_params.py">params</a>) -> <a href="./src/cadenya/types/objectives/objective_feedback.py">SyncCursorPagination[ObjectiveFeedback]</a></code>

# MemoryLayers

Types:

```python
from cadenya.types import MemoryLayer, MemoryLayerInfo, MemoryLayerSpec
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/memory_layers">client.memory_layers.<a href="./src/cadenya/resources/memory_layers/memory_layers.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/memory_layer_create_params.py">params</a>) -> <a href="./src/cadenya/types/memory_layer.py">MemoryLayer</a></code>
- <code title="get /v1/workspaces/{workspaceId}/memory_layers/{id}">client.memory_layers.<a href="./src/cadenya/resources/memory_layers/memory_layers.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/memory_layer.py">MemoryLayer</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/memory_layers/{id}">client.memory_layers.<a href="./src/cadenya/resources/memory_layers/memory_layers.py">update</a>(id, \*, workspace_id, \*\*<a href="src/cadenya/types/memory_layer_update_params.py">params</a>) -> <a href="./src/cadenya/types/memory_layer.py">MemoryLayer</a></code>
- <code title="get /v1/workspaces/{workspaceId}/memory_layers">client.memory_layers.<a href="./src/cadenya/resources/memory_layers/memory_layers.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/memory_layer_list_params.py">params</a>) -> <a href="./src/cadenya/types/memory_layer.py">SyncCursorPagination[MemoryLayer]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/memory_layers/{id}">client.memory_layers.<a href="./src/cadenya/resources/memory_layers/memory_layers.py">delete</a>(id, \*, workspace_id) -> None</code>

## Entries

Types:

```python
from cadenya.types.memory_layers import (
    MemoryEntry,
    MemoryEntryCreateSpec,
    MemoryEntryCreateSpecContent,
    MemoryEntryCreateSpecUploadID,
    MemoryEntryDetail,
    MemoryEntryInfo,
    MemoryEntrySpec,
    MemoryEntryUpdateSpec,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/memory_layers/{memoryLayerId}/entries">client.memory_layers.entries.<a href="./src/cadenya/resources/memory_layers/entries.py">create</a>(memory_layer_id, \*, workspace_id, \*\*<a href="src/cadenya/types/memory_layers/entry_create_params.py">params</a>) -> <a href="./src/cadenya/types/memory_layers/memory_entry_detail.py">MemoryEntryDetail</a></code>
- <code title="get /v1/workspaces/{workspaceId}/memory_layers/{memoryLayerId}/entries/{id}">client.memory_layers.entries.<a href="./src/cadenya/resources/memory_layers/entries.py">retrieve</a>(memory_layer_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/memory_layers/memory_entry_detail.py">MemoryEntryDetail</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/memory_layers/{memoryLayerId}/entries/{id}">client.memory_layers.entries.<a href="./src/cadenya/resources/memory_layers/entries.py">update</a>(memory_layer_id, id, \*, workspace_id, \*\*<a href="src/cadenya/types/memory_layers/entry_update_params.py">params</a>) -> <a href="./src/cadenya/types/memory_layers/memory_entry_detail.py">MemoryEntryDetail</a></code>
- <code title="get /v1/workspaces/{workspaceId}/memory_layers/{memoryLayerId}/entries">client.memory_layers.entries.<a href="./src/cadenya/resources/memory_layers/entries.py">list</a>(memory_layer_id, \*, workspace_id, \*\*<a href="src/cadenya/types/memory_layers/entry_list_params.py">params</a>) -> <a href="./src/cadenya/types/memory_layers/memory_entry.py">SyncCursorPagination[MemoryEntry]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/memory_layers/{memoryLayerId}/entries/{id}">client.memory_layers.entries.<a href="./src/cadenya/resources/memory_layers/entries.py">delete</a>(memory_layer_id, id, \*, workspace_id) -> None</code>

# Uploads

Types:

```python
from cadenya.types import Upload, UploadInfo, UploadSpec
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/uploads">client.uploads.<a href="./src/cadenya/resources/uploads.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/upload_create_params.py">params</a>) -> <a href="./src/cadenya/types/upload.py">Upload</a></code>
- <code title="get /v1/workspaces/{workspaceId}/uploads/{id}">client.uploads.<a href="./src/cadenya/resources/uploads.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/upload.py">Upload</a></code>

# Models

Types:

```python
from cadenya.types import Model, ModelSpec
```

Methods:

- <code title="get /v1/workspaces/{workspaceId}/models/{id}">client.models.<a href="./src/cadenya/resources/models.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/model.py">Model</a></code>
- <code title="get /v1/workspaces/{workspaceId}/models">client.models.<a href="./src/cadenya/resources/models.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/model_list_params.py">params</a>) -> <a href="./src/cadenya/types/model.py">SyncCursorPagination[Model]</a></code>
- <code title="post /v1/workspaces/{workspaceId}/models/{id}:disable">client.models.<a href="./src/cadenya/resources/models.py">disable</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/model.py">Model</a></code>
- <code title="post /v1/workspaces/{workspaceId}/models/{id}:enable">client.models.<a href="./src/cadenya/resources/models.py">enable</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/model.py">Model</a></code>
- <code title="post /v1/workspaces/{workspaceId}/models:swapModelOnVariations">client.models.<a href="./src/cadenya/resources/models.py">swap</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/model_swap_params.py">params</a>) -> object</code>

# Search

Types:

```python
from cadenya.types import SearchSearchToolsOrToolSetsResponse
```

Methods:

- <code title="get /v1/workspaces/{workspaceId}/search/tools_or_tool_sets">client.search.<a href="./src/cadenya/resources/search.py">search_tools_or_tool_sets</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/search_search_tools_or_tool_sets_params.py">params</a>) -> <a href="./src/cadenya/types/search_search_tools_or_tool_sets_response.py">SearchSearchToolsOrToolSetsResponse</a></code>

# ToolSets

Types:

```python
from cadenya.types import (
    ApprovalRequirementFilter,
    ApprovalRequirementFilterAlways,
    ApprovalRequirementFilterOnly,
    AttributeFilter,
    StringMatcher,
    StringMatcherContains,
    StringMatcherEndsWith,
    StringMatcherExact,
    StringMatcherRegex,
    StringMatcherStartsWith,
    SyncCompleted,
    SyncFailed,
    SyncStarted,
    ToolFilter,
    ToolSet,
    ToolSetAdapter,
    ToolSetAdapterBare,
    ToolSetAdapterBareVariant,
    ToolSetAdapterHTTP,
    ToolSetAdapterHTTPVariant,
    ToolSetAdapterMCP,
    ToolSetAdapterMCPVariant,
    ToolSetAdapterOpenAPI,
    ToolSetAdapterOpenAPIUploadID,
    ToolSetAdapterOpenAPIURL,
    ToolSetAdapterOpenAPIVariant,
    ToolSetEvent,
    ToolSetEventData,
    ToolSetEventDataSyncCompleted,
    ToolSetEventDataSyncFailed,
    ToolSetEventDataSyncStarted,
    ToolSetInfo,
    ToolSetSpec,
    ToolSetUsage,
    ToolSetGetOpenAPISpecResponse,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/tool_sets">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/tool_set_create_params.py">params</a>) -> <a href="./src/cadenya/types/tool_set.py">ToolSet</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{id}">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_set.py">ToolSet</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/tool_sets/{id}">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">update</a>(id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_set_update_params.py">params</a>) -> <a href="./src/cadenya/types/tool_set.py">ToolSet</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/tool_set_list_params.py">params</a>) -> <a href="./src/cadenya/types/tool_set.py">SyncCursorPagination[ToolSet]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/tool_sets/{id}">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">delete</a>(id, \*, workspace_id) -> None</code>
- <code title="post /v1/workspaces/{workspaceId}/tool_sets/{id}:archive">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">archive</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_set.py">ToolSet</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/openapi_spec">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">get_openapi_spec</a>(tool_set_id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_set_get_openapi_spec_response.py">ToolSetGetOpenAPISpecResponse</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/events">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">list_events</a>(tool_set_id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_set_list_events_params.py">params</a>) -> <a href="./src/cadenya/types/tool_set_event.py">SyncCursorPagination[ToolSetEvent]</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/usage">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">list_usage</a>(tool_set_id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_set_list_usage_params.py">params</a>) -> <a href="./src/cadenya/types/tool_set_usage.py">SyncCursorPagination[ToolSetUsage]</a></code>
- <code title="post /v1/workspaces/{workspaceId}/tool_sets/{id}:unarchive">client.tool_sets.<a href="./src/cadenya/resources/tool_sets/tool_sets.py">unarchive</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_set.py">ToolSet</a></code>

## Tools

Types:

```python
from cadenya.types.tool_sets import (
    ConfigBare,
    ConfigHTTP,
    ConfigMCP,
    ConfigOpenAPI,
    MCPAnnotations,
    Tool,
    ToolInfo,
    ToolSpec,
    ToolSpecConfig,
    ToolSpecConfigBare,
    ToolSpecConfigHTTP,
    ToolSpecConfigMCP,
    ToolSpecConfigOpenAPI,
)
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">create</a>(tool_set_id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_sets/tool_create_params.py">params</a>) -> <a href="./src/cadenya/types/tool_sets/tool.py">Tool</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools/{id}">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">retrieve</a>(tool_set_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_sets/tool.py">Tool</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools/{id}">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">update</a>(tool_set_id, id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_sets/tool_update_params.py">params</a>) -> <a href="./src/cadenya/types/tool_sets/tool.py">Tool</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">list</a>(tool_set_id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_sets/tool_list_params.py">params</a>) -> <a href="./src/cadenya/types/tool_sets/tool.py">SyncCursorPagination[Tool]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools/{id}">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">delete</a>(tool_set_id, id, \*, workspace_id) -> None</code>
- <code title="post /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools/{id}:omit">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">omit</a>(tool_set_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_sets/tool.py">Tool</a></code>
- <code title="post /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/tools/{id}:restore">client.tool_sets.tools.<a href="./src/cadenya/resources/tool_sets/tools.py">restore</a>(tool_set_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_sets/tool.py">Tool</a></code>

## Secrets

Types:

```python
from cadenya.types.tool_sets import ToolSetSecret, ToolSetSecretInfo, ToolSetSecretSpec
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/secrets">client.tool_sets.secrets.<a href="./src/cadenya/resources/tool_sets/secrets.py">create</a>(tool_set_id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_sets/secret_create_params.py">params</a>) -> <a href="./src/cadenya/types/tool_sets/tool_set_secret.py">ToolSetSecret</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/secrets/{id}">client.tool_sets.secrets.<a href="./src/cadenya/resources/tool_sets/secrets.py">retrieve</a>(tool_set_id, id, \*, workspace_id) -> <a href="./src/cadenya/types/tool_sets/tool_set_secret.py">ToolSetSecret</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/secrets/{id}">client.tool_sets.secrets.<a href="./src/cadenya/resources/tool_sets/secrets.py">update</a>(tool_set_id, id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_sets/secret_update_params.py">params</a>) -> <a href="./src/cadenya/types/tool_sets/tool_set_secret.py">ToolSetSecret</a></code>
- <code title="get /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/secrets">client.tool_sets.secrets.<a href="./src/cadenya/resources/tool_sets/secrets.py">list</a>(tool_set_id, \*, workspace_id, \*\*<a href="src/cadenya/types/tool_sets/secret_list_params.py">params</a>) -> <a href="./src/cadenya/types/tool_sets/tool_set_secret.py">SyncCursorPagination[ToolSetSecret]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/tool_sets/{toolSetId}/secrets/{id}">client.tool_sets.secrets.<a href="./src/cadenya/resources/tool_sets/secrets.py">delete</a>(tool_set_id, id, \*, workspace_id) -> None</code>

# APIKeys

Types:

```python
from cadenya.types import APIKey, APIKeyInfo, APIKeySpec
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/api_keys">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/api_key_create_params.py">params</a>) -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="get /v1/workspaces/{workspaceId}/api_keys/{id}">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/api_keys/{id}">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">update</a>(id, \*, workspace_id, \*\*<a href="src/cadenya/types/api_key_update_params.py">params</a>) -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="get /v1/workspaces/{workspaceId}/api_keys">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/api_key_list_params.py">params</a>) -> <a href="./src/cadenya/types/api_key.py">SyncCursorPagination[APIKey]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/api_keys/{id}">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">delete</a>(id, \*, workspace_id) -> None</code>
- <code title="post /v1/workspaces/{workspaceId}/api_keys/{id}:disable">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">disable</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="post /v1/workspaces/{workspaceId}/api_keys/{id}:enable">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">enable</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="post /v1/workspaces/{workspaceId}/api_keys/{id}:rotate">client.api_keys.<a href="./src/cadenya/resources/api_keys.py">rotate</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>

# GlobalAPIKey

Methods:

- <code title="get /v1/account/global_api_key">client.global_api_key.<a href="./src/cadenya/resources/global_api_key.py">retrieve</a>() -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="post /v1/account/global_api_key:disable">client.global_api_key.<a href="./src/cadenya/resources/global_api_key.py">disable</a>() -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="post /v1/account/global_api_key:enable">client.global_api_key.<a href="./src/cadenya/resources/global_api_key.py">enable</a>() -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>
- <code title="post /v1/account/global_api_key:rotate">client.global_api_key.<a href="./src/cadenya/resources/global_api_key.py">rotate</a>() -> <a href="./src/cadenya/types/api_key.py">APIKey</a></code>

# WorkspaceSecrets

Types:

```python
from cadenya.types import WorkspaceSecret, WorkspaceSecretInfo, WorkspaceSecretSpec
```

Methods:

- <code title="post /v1/workspaces/{workspaceId}/workspace_secrets">client.workspace_secrets.<a href="./src/cadenya/resources/workspace_secrets.py">create</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/workspace_secret_create_params.py">params</a>) -> <a href="./src/cadenya/types/workspace_secret.py">WorkspaceSecret</a></code>
- <code title="get /v1/workspaces/{workspaceId}/workspace_secrets/{id}">client.workspace_secrets.<a href="./src/cadenya/resources/workspace_secrets.py">retrieve</a>(id, \*, workspace_id) -> <a href="./src/cadenya/types/workspace_secret.py">WorkspaceSecret</a></code>
- <code title="patch /v1/workspaces/{workspaceId}/workspace_secrets/{id}">client.workspace_secrets.<a href="./src/cadenya/resources/workspace_secrets.py">update</a>(id, \*, workspace_id, \*\*<a href="src/cadenya/types/workspace_secret_update_params.py">params</a>) -> <a href="./src/cadenya/types/workspace_secret.py">WorkspaceSecret</a></code>
- <code title="get /v1/workspaces/{workspaceId}/workspace_secrets">client.workspace_secrets.<a href="./src/cadenya/resources/workspace_secrets.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/workspace_secret_list_params.py">params</a>) -> <a href="./src/cadenya/types/workspace_secret.py">SyncCursorPagination[WorkspaceSecret]</a></code>
- <code title="delete /v1/workspaces/{workspaceId}/workspace_secrets/{id}">client.workspace_secrets.<a href="./src/cadenya/resources/workspace_secrets.py">delete</a>(id, \*, workspace_id) -> None</code>

# Workspaces

Types:

```python
from cadenya.types import Workspace, WorkspaceSpec
```

Methods:

- <code title="get /v1/workspaces">client.workspaces.<a href="./src/cadenya/resources/workspaces.py">list</a>(\*\*<a href="src/cadenya/types/workspace_list_params.py">params</a>) -> <a href="./src/cadenya/types/workspace.py">SyncCursorPagination[Workspace]</a></code>

# WorkspaceAdmin

Types:

```python
from cadenya.types import WorkspaceMember
```

Methods:

- <code title="post /v1/account/workspaces">client.workspace_admin.<a href="./src/cadenya/resources/workspace_admin/workspace_admin.py">create</a>(\*\*<a href="src/cadenya/types/workspace_admin_create_params.py">params</a>) -> <a href="./src/cadenya/types/workspace.py">Workspace</a></code>
- <code title="get /v1/account/workspaces/{workspaceId}">client.workspace_admin.<a href="./src/cadenya/resources/workspace_admin/workspace_admin.py">retrieve</a>(\*, workspace_id) -> <a href="./src/cadenya/types/workspace.py">Workspace</a></code>
- <code title="patch /v1/account/workspaces/{workspaceId}">client.workspace_admin.<a href="./src/cadenya/resources/workspace_admin/workspace_admin.py">update</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/workspace_admin_update_params.py">params</a>) -> <a href="./src/cadenya/types/workspace.py">Workspace</a></code>
- <code title="get /v1/account/workspaces">client.workspace_admin.<a href="./src/cadenya/resources/workspace_admin/workspace_admin.py">list</a>(\*\*<a href="src/cadenya/types/workspace_admin_list_params.py">params</a>) -> <a href="./src/cadenya/types/workspace.py">SyncCursorPagination[Workspace]</a></code>
- <code title="delete /v1/account/workspaces/{workspaceId}">client.workspace_admin.<a href="./src/cadenya/resources/workspace_admin/workspace_admin.py">archive</a>(\*, workspace_id) -> None</code>

## Members

Methods:

- <code title="get /v1/account/workspaces/{workspaceId}/members">client.workspace_admin.members.<a href="./src/cadenya/resources/workspace_admin/members.py">list</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/workspace_admin/member_list_params.py">params</a>) -> <a href="./src/cadenya/types/workspace_member.py">SyncCursorPagination[WorkspaceMember]</a></code>
- <code title="post /v1/account/workspaces/{workspaceId}/members">client.workspace_admin.members.<a href="./src/cadenya/resources/workspace_admin/members.py">add</a>(\*, workspace_id, \*\*<a href="src/cadenya/types/workspace_admin/member_add_params.py">params</a>) -> <a href="./src/cadenya/types/workspace_member.py">WorkspaceMember</a></code>
- <code title="delete /v1/account/workspaces/{workspaceId}/members/{profileId}">client.workspace_admin.members.<a href="./src/cadenya/resources/workspace_admin/members.py">remove</a>(profile_id, \*, workspace_id) -> None</code>

## Profiles

Methods:

- <code title="get /v1/account/profiles">client.workspace_admin.profiles.<a href="./src/cadenya/resources/workspace_admin/profiles.py">list</a>(\*\*<a href="src/cadenya/types/workspace_admin/profile_list_params.py">params</a>) -> <a href="./src/cadenya/types/profile.py">SyncCursorPagination[Profile]</a></code>

# Webhooks

Types:

```python
from cadenya.types import UnsafeUnwrapWebhookEvent, UnwrapWebhookEvent
```
