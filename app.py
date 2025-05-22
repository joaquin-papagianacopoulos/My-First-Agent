import os
from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

# ✅ Clave de OpenRouter
os.environ["OPENROUTER_API_KEY"] = "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"

# ✅ Configuración del modelo Mixtral para asistentes
llm_config = {
    "config_list": [
        {
            "model": "gpt-4o-mini",
            "base_url": "https://openrouter.ai/api/v1",
            "api_key": os.environ["OPENROUTER_API_KEY"]
        }
    ]
}

# 🎭 Agentes
escritor = AssistantAgent(
    name="Escritor",
    system_message="Sos un redactor profesional. Redactá artículos claros y bien estructurados.",
    llm_config=llm_config
)

editor = AssistantAgent(
    name="Editor",
    system_message="Sos un editor crítico. Revisá textos y hacé sugerencias claras y constructivas.",
    llm_config=llm_config
)

usuario = UserProxyAgent(
    name="Usuario",
    code_execution_config={"use_docker": False}
)

# 💬 Grupo de chat
groupchat = GroupChat(
    agents=[usuario, escritor, editor],
    messages=[],
    max_round=5,
    select_speaker_auto_llm_config=llm_config
)

manager = GroupChatManager(groupchat=groupchat)

# 🚀 Iniciamos la conversación
usuario.initiate_chat(
    manager,
    message="Escribí un artículo de 150 palabras sobre 'El futuro de la inteligencia artificial'."
)
