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
      observaciones: "esta pedio el socio",
      hora_inicio: "",
      hora_termino: "0:0",
      id_paciente: "",
      fecha: "",
      loading: true
    };
  };

  fetchData = async () => {
    var hora = new Date().getHours()
    var minutos = new Date().getMinutes()
    var horainicio = hora + ":" + minutos
    this.setState({ id_paciente: this.props.navigation.state.params.pacienteactual.id_paciente })
    this.setState({ hora_inicio: horainicio })
    this.setState({ fecha: this.props.navigation.state.params.fecha })
  }

  finalizarVisita = async () => {
    var hora = new Date().getHours()
    var minutos = new Date().getMinutes()
    var horatermino = hora + ":" + minutos
    this.setState({ hora_termino: horatermino })
    var datosvisita = this.state.edad + "*" + this.state.diagnostico + "*" + this.state.signos_vitales + "*" + this.state.observaciones
    var data = { horainicio: this.state.hora_inicio, horatermino, observaciones: datosvisita, idpaciente: this.state.id_paciente, fecha: this.state.fecha }
    const options = {
      method: 'POST', // or 'PUT'
      body: JSON.stringify(data), // data can be `string` or {object}!
      headers: {
        'Content-Type': 'application/json'
      }
    }
    this.props.navigation.navigate('Home')
    const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/detallevisita', options);
    const personal = await response.json();

  }
  saludo = () => { Alert.alert("Wena CTM!") }
  fventas = () => {
    this.saludo;
    //this.props.navigation.navigate('ventas')
    //console.log("paso aqui :c");    
  }
  componentDidMount() {
    this.fetchData();
  }

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.buttoncontainer}>
          <Text style={styles.texto1} >Ingresar detalles de visita por aca</Text>
          <Text  style={styles.texto1} >Edad del paciente:</Text>
          <TextInput onChangeText={(text) => this.setState({ edad: text })} style={styles.input1}></TextInput>
          <Text style={styles.texto1} >Diagnostico:</Text>
          <TextInput onChangeText={(text) => this.setState({ diagnostico: text })} style={styles.input1}></TextInput>
          <Text style={styles.texto1} >Signos Vitales:</Text>
          <TextInput onChangeText={(text) => this.setState({ signos_vitales: text })} style={styles.input1}></TextInput>
          <Text style={styles.texto1} >Observaciones:</Text>
          <TextInput onChangeText={(text) => this.setState({ observaciones: text })} style={styles.input1}></TextInput>
          <TouchableOpacity style={styles.button1} onPress={() => this.finalizarVisita()}>
            <Text style={styles.buttontext1}>Finalizar Visita</Text>
          </TouchableOpacity>
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
    marginTop: 20

  },
  input1: {
    borderBottomColor: 'black',
    borderBottomWidth: 1,
    fontSize: 20,
    maxWidth: "90%",
    marginHorizontal: 15,
    marginVertical: 10,
    paddingHorizontal: 100
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
  },
  texto1: {
    paddingHorizontal: 15,
    fontSize: 20,
    paddingVertical: 2
  }
})

export default home

