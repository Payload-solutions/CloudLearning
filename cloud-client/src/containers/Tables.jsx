import React, { useEffect, useState } from 'react';
import "../assets/styles/components/Tables.scss"

/**
 *@author Arturo Negreiros
 * this sections will contain the values extracted from the database, that is, cassandra sql
 */


const Tables = () => {
    const [numbers, Setnumbers] = useState([]);
    const [bacterias, Setbacterias] = useState([]);
    const [times, Settime] = useState([]);

    const APIFlask = "http://192.168.100.8:4000/bacteria";
    useEffect(() => {
        fetch(APIFlask)
            .then(response => response.json())
            .then(data => Settime(data.time) || Setbacterias(data.bacteria) || Setnumbers(data.datas))
    }, []);

    // console.log(bacterias);
    // console.log(times);
    console.log(bacterias);
    return (
        <div>
            <div className="table_content">
                <div className="row">
                    <div className="col-md-6">
                        <table className="table">
                            <thead>
                                <tr>
                                    <th scope="col">Indice</th>
                                    <th scope="col">Tiempo</th>
                                    <th scope="col">Crecimiento logarítimico</th>
                                </tr>
                            </thead>
                            <tbody>
                                {
                                    numbers.map(element =>
                                        <tr key={element.id}>
                                            <td>{element.id}</td>
                                            <td> {element.time}</td>
                                            <td> {element.bacteria}</td>
                                        </tr>

                                    )
                                }
                            </tbody>
                        </table>
                    </div>
                    <div className="col-md-6">
                        <div className="containter p-2">
                            <div className="row">
                                <div className="col-md-12" id="card__content_table">
                                    <div className="card">
                                        <div className="card-header">
                                            <h5 className="card-title">Crecimiento bacteriano</h5>
                                        </div>
                                        <div className="card-body">
                                            <p className="card-text">Con los valores anteriores, permiten visualizar, como el crecimiento
                                                bacteriano es de manera logarítmica, permitiendo ver como a través del tiempo
                                                crece
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="containter p-2">
                            <div className="row">
                                <div className="col-md-12" id="card__content_table">
                                    <div className="card">
                                        <div className="card-header">
                                            <h5 className="card-title">Crecimiento bacteriano</h5>
                                        </div>
                                        <div className="card-body">
                                            <p className="card-text">Con los valores anteriores, permiten visualizar, como el crecimiento
                                                bacteriano es de manera logarítmica, permitiendo ver como a través del tiempo
                                                crece
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="containter p-2">
                            <div className="row">
                                <div className="col-md-12" id="card__content_table">
                                    <div className="card">
                                        <div className="card-header">
                                            <h5 className="card-title">Crecimiento bacteriano</h5>
                                        </div>
                                        <div className="card-body">
                                            <p className="card-text">Con los valores anteriores, permiten visualizar, como el crecimiento
                                                bacteriano es de manera logarítmica, permitiendo ver como a través del tiempo
                                                crece
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>



        </div>
    );
}

export default Tables;