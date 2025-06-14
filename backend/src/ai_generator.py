import os
import json

from openai import OpenAI
from typing import Any, Dict
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """Você é um especialista em criação de desafios de programação.
    Sua tarefa é gerar uma pergunta de codificação com múltiplas escolhas de resposta.
    A pergunta deve ser adequada ao nível de dificuldade especificado.

    Para questões fáceis: Foque em sintaxe básica, operações simples ou conceitos comuns de programação.

    Para questões médias: Aborde conceitos intermediários como estruturas de dados, algoritmos ou recursos da linguagem.

    Para questões difíceis: Inclua tópicos avançados, padrões de design, técnicas de otimização ou algoritmos complexos.

    Retorne o desafio no seguinte formato JSON:
    
    {
        "title": "O título da pergunta",
        "options": ["Opção 1", "Opção 2", "Opção 3", "Opção 4"],
        "correct_answer_id": 0, // Índice da resposta correta (0-3)
        "explanation": "Explicação detalhada do porquê a resposta correta está certa"
    }
    
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty coding challenge."}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        challenge_data = json.loads(content)
        
        required_fields = ["title", "options", "corrent_answer_id", "explanation"]
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"Missing required field: {field}")
    
    except Exception as e:
        print (e)
        
        return {
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list."
        }
        