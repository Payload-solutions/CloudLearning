import React from 'react';
import '../assets/styles/components/About.scss'
import { Card, Button, Jumbotron, Container } from 'react-bootstrap';

const About = () => (
    <section className="main">
        <h2 className="main__title">¿Quienes somos nosotros?</h2>
        
        <p>En nuestro proyecto, queremos demostrar, cuan importante es el
            uso de la tecnología en la agricultura.
        </p>
        <p>
            Utilizamos redes neuronales, capaces de predecir el crecimiento
            bacteriano y capaces de clasificar los diferentes tipos de productos
            de yogur en vase a sus variables principales.
        </p>
        {/* <Jumbotron>
            <Container>
                <h1>Fluid jumbotron !</h1>
                <p>
                    This is a modified fluid jumbotron which
                    stretches the whole horizontal space.
                </p>
                <Button variant="primary">
                    Primary Button
                </Button>
            </Container>
        </Jumbotron> */}
        {/* <Card>
            <Card.Header>Featured</Card.Header>
            <Card.Body>
                <Card.Title>Special title treatment</Card.Title>
                <Card.Text>
                    With supporting text below as a natural lead-in to additional content.
                </Card.Text>
                <Button variant="primary">Go somewhere</Button>
            </Card.Body>
        </Card> */}
    </section>

);

export default About;