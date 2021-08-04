import React, { useEffect, useState } from 'react';
import "../assets/styles/components/Tables.scss"
/**
 *@author Arturo Negreiros
 * this sections will contain the values extracted from the database, that is, cassandra sql
 */


const Tables = () => {
    const [numbers, Setnumbers] = useState([]);
    const APIFlsk = "http://192.168.100.8:5000/test";
    useEffect(() => {
        fetch(APIFlsk)
            .then(response => response.json())
            .then(data => Setnumbers(data))
    }, []);
    console.log(numbers)
    return (
        <div className="table_content">
            <table className="table">
                <thead>
                    <tr>
                        <th scope="col">pH</th>
                        <th scope="col">Acidez</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                    </tr>
                </thead>
            </table>
        </div>
    );
}

export default Tables;