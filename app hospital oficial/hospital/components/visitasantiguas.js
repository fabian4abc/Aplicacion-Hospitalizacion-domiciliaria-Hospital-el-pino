import { Component } from 'react'
import { StyleSheet, Text, View, Image, Button, Alert, TouchableOpacity, TextInput } from 'react-native'
import React from 'react'


class home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            edad: "",
            diagnostico: "",
            signos_vitales: "",
            observaciones: "",
            id_paciente: "",
            fecha: "",
            loading: true
        };
    };
    /*
      fetchData = async () => {
        var hora = new Date().getHours()
        var minutos = new Date().getMinutes()
        var horainicio = hora + ":" + minutos
        this.setState({ id_paciente: this.props.navigation.state.params.pacienteactual.id_paciente })
        this.setState({ hora_inicio: horainicio })
        this.setState({ fecha: this.props.navigation.state.params.fecha })
      }
    
      finalizarVisita = async () => {
        var datosvisita = this.state.edad + "*" + this.state.diagnostico + "*" + this.state.signos_vitales + "*" + this.state.observaciones
        var data = { horainicio: this.state.hora_inicio, horatermino: this.state.hora_termino, observaciones: datosvisita, idpaciente: this.state.id_paciente, fecha: this.state.fecha }
        const options = {
          method: 'POST', // or 'PUT'
          body: JSON.stringify(data), // data can be `string` or {object}!
          headers: {
            'Content-Type': 'application/json'
          }
        }
        this.props.navigation.navigate('Home')
        const response = await fetch('http://localhost:1348/detallevisita', options);
        const personal = await response.json();
    
      }
      saludo = () => { Alert.alert("Wena CTM!") }
      fventas = () => {
        this.saludo;
        //this.props.navigation.navigate('ventas')
        //console.log("paso aqui :c");    
      }
      
    */
    componentDidMount() {
        var detalle = this.props.navigation.state.params.observaciones
        //alert(detalle)
        var detallesplit = detalle.split("*")
        this.setState({ edad: detallesplit[0], diagnostico: detallesplit[1], signos_vitales: detallesplit[2], observaciones: detallesplit[3] })
    }
    render() {
        return (
            <View style={styles.container}>
                <View style={styles.buttoncontainer}>
                    <Text style={styles.texto1}>Nombre: {this.props.navigation.state.params.nombre } {this.props.navigation.state.params.apellido1 }  </Text>
                    <Text style={styles.texto1}>Edad del paciente: {this.state.edad }</Text>
                    <Text style={styles.texto1}>Diagnostico: {this.state.diagnostico }</Text>
                    <Text style={styles.texto1}>Signos Vitales: {this.state.signos_vitales }</Text>
                    <Text style={styles.texto1}>Observaciones: {this.state.observaciones }</Text>
                    <Image style={styles.logo} source={require("../assets/logo.png")}></Image>
                </View>

            </View>

        )
    }
}
const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: 'column'
    },
    buttoncontainer: {
        flex: 5,
        flexDirection: 'column',
        justifyContent: "flex-start",
        alignItems: "center",
        marginTop: 60

    },
    input1: {
        borderBottomColor: 'black',
        borderBottomWidth: 1,
        fontSize: 20,
        maxWidth: "90%",
        marginHorizontal: 15,
        marginVertical: 10
    },
    logo: {
        width: 300,
        height: 300,
        justifyContent: "center",
        alignItems: "center",
        alignContent: "center"
    },
    button1: {
        elevation: 10,
        backgroundColor: "#009688",
        borderRadius: 10,
        paddingVertical: 10,
        paddingHorizontal: 10,
        marginVertical: 10,
        minWidth: "70%",
        borderRadius: 30
    },
    texto1: {
        paddingHorizontal: 15,
        fontSize: 20,
        paddingVertical: 10,
        textAlign: "left"
    },
    buttontext1: {
        fontSize: 18,
        color: "#fff",
        fontWeight: "bold",
        alignSelf: "center",
        textTransform: "uppercase"
    },
    negrita: {
        fontWeight: "bold"
    },
    header: {
        flex: 0.05,
        flexDirection: 'row',
        marginTop: 40,
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#c1bfbf"
    },
    body: {
        flex: 0.2,
        alignItems: 'center',
        marginBottom: 150,
        marginTop: 0
    },
    footer: {
        flex: 0.5,
        alignItems: 'center',
        justifyContent: "flex-end",
        position: "relative",
        bottom: 0,
    }
})

export default home

