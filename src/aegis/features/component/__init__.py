import logging

from aegis.features import env_fs, Feature
from aegis.features.component.data_models import ComponentIntelligenceModel

logger = logging.getLogger(__name__)


class ComponentIntelligence(Feature):
    """Based on supplied component name and rh context generate a component 'card' of information."""

    async def exec(self, component_name):
        template = env_fs.get_template("component/component_intelligence_prompt.txt")
        prompt = template.render(
            {
                "context": component_name,
                "schema": ComponentIntelligenceModel.model_json_schema(),
            }
        )
        logger.debug(prompt)
        return await self.agent.run(prompt, output_type=ComponentIntelligenceModel)
