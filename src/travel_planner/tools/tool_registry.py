"""Shared tool registry to avoid duplicate instances and improve performance."""

class ToolRegistry:
    """Registry for shared tool instances to improve performance."""

    _instances = {}

    @classmethod
    def get_tool(cls, tool_class):
        """Get or create a shared tool instance."""
        tool_name = tool_class.__name__

        if tool_name not in cls._instances:
            cls._instances[tool_name] = tool_class()

        return cls._instances[tool_name]

    @classmethod
    def clear_cache(cls):
        """Clear all cached tool instances."""
        cls._instances.clear()