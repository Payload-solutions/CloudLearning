import React, { useEffect, useState } from 'react';
import APIFLASKM1 from '../links/links';
import { Line } from 'react-chartjs-2';

const Chartvalues = () => {

    const [accuracies, Setaccuracies] = useState([]);
    const [losses, Setlosses] = useState([]);
    const [maelacts, Setmaelacts] = useState([]);
    const [maestrep, Setmaestrep] = useState([]);

    // const APIFLASKM1 = "http://127.0.0.1:5000/charting";
    useEffect(() => {
        fetch(APIFLASKM1)
            .then(response => response.json())
            .then(data => Setaccuracies(data.classification.accuracy) || Setlosses(data.classification.loss) ||
                Setmaelacts(data.maelact) || Setmaestrep(data.maestrep))
    }, [])
    console.log(maestrep[0]);

    let labelStack = [];

    for (let i=1; i < 81; i++){
        labelStack.push(i)
    }

    const state = {


        labels: labelStack,
        datasets: [
            {
                label: 'Mean absolute error',
                fill: false,
                lineTension: 0.5,
                backgroundColor: 'rgba(75,192,192,1)',
                borderColor: 'rgba(0,0,0,1)',
                borderWidth: 2,
                data: maestrep
            }
        ]
    }

    return (
        <div className="container p-4">
            <Line
                data={state}
                options={{
                    title: {
                        display: true,
                        text: 'Average Rainfall per month',
                        fontSize: 20
                    },
                    legend: {
                        display: true,
                        position: 'right'
                    }
                }}
            />
            <Line
                data={state}
                options={{
                    title: {
                        display: true,
                        text: 'Average Rainfall per month',
                        fontSize: 20
                    },
                    legend: {
                        display: true,
                        position: 'right'
                    }
                }}
            />
        </div>
    );
}

export default Chartvalues;