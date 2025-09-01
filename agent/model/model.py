from langchain_openai import ChatOpenAI


def get_model(model_name, temperature, timeout, api_key, **kwargs):
    """
    Returns a language model instance for the specified model name.
    Additional keyword arguments are passed to the model constructor.
    """
    return ChatOpenAI(
        model=model_name,
        temperature=temperature,
        timeout=timeout,
        api_key=api_key,
        **kwargs,
    )
