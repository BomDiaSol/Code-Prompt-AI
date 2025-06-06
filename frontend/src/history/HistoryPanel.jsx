import "react"
import {useState, useEffect} from "react"
import {MCQChallenge} from "../challenge/MCQChallenge.jsx";
import {useApi} from "../utils/api.js";

export function HistoryPanel() {
    const {makeRequest} = useApi()
    const [history, setHistory] = useState([])
    const [isLoading, setIsLoading] = useState(true)
    const [error, setError] = useState(null)

    useEffect(() => {
        fetchHistory()
    }, [])

    const fetchHistory = async () => {
        setIsLoading(false)
    }

    if (isLoading) {
        return <div className="loading">Carregando seu histórico...</div>
    }

    if (error) {
        return <div className="error-message">
            <p>{error}</p>
            <button onClick={fetchHistory}>Tente novamente</button>
        </div>
    }

    return <div className="history-panel">
        <h2>History</h2>
        {history.length === 0 ? <p>Sem histórico de desafios</p> :
            <div className="history-list">
                {history.map((challenge) => {
                    return <MCQChallenge
                                challenge={challenge}
                                key={challenge.id}
                                showExplanation
                            />
                })}
            </div>
        }
    </div>
}