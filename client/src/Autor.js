import React, { Component } from 'react';
import dateFormat from 'dateformat';
import './css/main.css';
import Alert from 'react-s-alert';
import 'react-s-alert/dist/s-alert-default.css';

export default class Autor extends Component {

    constructor() {
        super();
        this.state = {nome_autor: '', data_nasc: ''};
    }

    enviaDados(evento) {
        evento.preventDefault();

        const requestInfo = {
            method: 'POST',
            body: JSON.stringify({nome_autor:this.nome_autor.value, data_nasc:this.data_nasc.value}),
            headers: new Headers({
                'Content-type': 'application/json'
            })
        };

        fetch('http://localhost:8000/autores.json', requestInfo)
            .then((response) => {
                if(response.ok) {
                    return response.json();
                } else {
                    throw new Error("Não foi possível enviar os dados")
                }
            })
            .then((nome_autor, data_nasc) => {
                this.setState({nome_autor})
                this.setState(dateFormat(data_nasc, "isoDate"))
                Alert.success('Autor cadastrado com sucesso.', {
                    position: 'top-right',
                    effect: 'slide',
                    timeout: 'none'
                })
                evento.target.reset();
            })
            .catch(error => {
                error.message()
                Alert.error('Não foi possível cadastrar o autor.')
            })
    }

    render() {
        return(
            <form className="form-action" onSubmit={this.enviaDados.bind(this)}>
                <div className="input-form-action">
                    <label htmlFor="nomeAutor">Nome</label>
                    <input type="text" name="nomeAutor" required ref={(input) => this.nome_autor = input}/>
                </div>
            
                <div className="input-form-action">
                    <label htmlFor="dataNasc">Data de Nascimento</label>
                    <input type="date" name="dataNasc" placeholder="DD/MM/AAAA" pattern="\d{2}\/\d{2}/\d{4}" required ref={(input) => this.data_nasc = input}/>
                </div>
                <button type="submit" className="botao-form-action">Enviar</button>
            </form>
       )
    }
}