import React, { useEffect, useState } from 'react';
import "../assets/styles/components/Tables.scss"
/**
 *@author Arturo Negreiros
 * this sections will contain the values extracted from the database, that is, cassandra sql
 */


const Tables = () => {
    const [numbers, Setnumbers] = useState([]);
    const APIFlsk = "http://192.168.100.8:4000/bacteria";
    useEffect(() => {
        fetch(APIFlsk)
            .then(response => response.json())
            .then(data => Setnumbers(data))
    }, []);
    // console.log(typeof(numbers.values))
    // console.log(Object.keys(numbers.values));
    let elements = JSON.stringify(numbers);
    console.log(elements);
    console.log(typeof(elements));
    return (
        <div>
            <div className="table_content">
                <table className="table">
                    <thead>
                        <tr>
                            <th scope="col">Tiempo</th>
                            <th scope="col">Crecimiento logarítimico</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            {/* {
                                numbers.values.map(item =>
                                 <td key={item.id}>item </td>
                            )} */}
                        </tr>
                    </tbody>
                </table>
            </div>


            <div className="containter p-4">
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

            <div className="table_content">
                <table className="table">
                    <thead>
                        <tr>
                            <th scope="col">Tiempo</th>
                            <th scope="col">Crecimiento logarítimico</th>
                        </tr>
                    </thead>
                </table>
            </div>
        </div>
    );
}

export default Tables;