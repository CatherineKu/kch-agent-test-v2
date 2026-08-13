# Copyright (c) 2025 Beijing Volcano Engine Technology Co., Ltd. and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from veadk import Agent
from veadk.tools.builtin_tools.web_search import web_search
from veadk.tools.builtin_tools.image_generate import image_generate

# 版本标记：每次更新代码时改这里，deploy 后调用 version_probe 即可确认线上是否为最新版本。
VERSION_MARKER = "v1"


def version_probe() -> dict[str, str]:
    """返回当前线上部署的版本标记，用于确认线上版本是否已随代码更新。

    当用户询问“版本”“更新了吗”“version”等问题时调用本工具，
    并把返回的 version 原样告知用户。

    Returns:
        一个包含版本标记的字典。
    """
    return {"version": VERSION_MARKER}


INSTRUCTION_AGENT = """你是一个专业、可靠的智能助手。

你的目标是准确理解用户的需求，并给出条理清晰、简洁有用的回答。

当用户询问版本或是否已更新时，调用 version_probe 工具并如实返回版本标记。

约束：
- 信息不足时主动提问澄清，不要臆造事实。
- 需要时合理调用可用的工具，并说明关键结论。
- 保持礼貌、专业的语气。"""

agent = Agent(
    name="kch_cicd_test",
    description="一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。",
    instruction=INSTRUCTION_AGENT,
    tools=[web_search, image_generate, version_probe],
    model_name="doubao-seed-2-1-pro-260628",
)

AGENT_DISPLAY_NAMES = {'kch_cicd_test': 'kch_cicd_test'}
AGENT_DRAFT = {'name': 'kch_cicd_test', 'description': '一个基于 VeADK 构建的智能助手，理解用户意图并调用合适的工具完成任务。', 'instruction': '你是一个专业、可靠的智能助手。\n\n你的目标是准确理解用户的需求，并给出条理清晰、简洁有用的回答。\n\n约束：\n- 信息不足时主动提问澄清，不要臆造事实。\n- 需要时合理调用可用的工具，并说明关键结论。\n- 保持礼貌、专业的语气。', 'agentType': 'llm', 'maxIterations': 3, 'a2aUrl': '', 'model': '', 'modelName': 'doubao-seed-2-1-pro-260628', 'modelProvider': '', 'modelApiBase': '', 'tools': [], 'skills': [], 'memory': {'shortTerm': False, 'longTerm': False}, 'knowledgebase': False, 'tracing': False, 'subAgents': [], 'builtinTools': ['web_search', 'image_generate'], 'customTools': [], 'mcpTools': [], 'a2aRegistry': {'enabled': False, 'registrySpaceId': '', 'registryTopK': '', 'registryRegion': '', 'registryEndpoint': ''}, 'shortTermBackend': 'local', 'longTermBackend': 'local', 'autoSaveSession': False, 'knowledgebaseBackend': 'viking', 'knowledgebaseIndex': '', 'tracingExporters': [], 'selectedSkills': [], 'workflow': None, 'deployment': {'feishuEnabled': False, 'envValues': {}}}

# ADK 加载器要求：顶层 agent 必须命名为 root_agent
root_agent = agent
