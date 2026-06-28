def build_source_context(sources):

    if not sources:
        return "No sources available."
    
    context = ""
    for i, source in enumerate(sources, 1):
        source_type = source.get('type', 'Unknown')
        content = source.get('content', '')
        name = source.get('name', f'Source {i}')
        
        context += f"[{i}] {name} ({source_type}):\n{content}\n\n"
    
    return context
