import { Component } from 'react'
import { StyleSheet, Text, View, Image, Button, Alert, TouchableOpacity, ImageBackground, TextInput } from 'react-native'
import { Icon } from 'react-native-elements'
import React from 'react'
import { createAppContainer } from 'react-navigation'
import { Assets, createStackNavigator } from 'react-navigation-stack'
import { Input } from 'react-native-elements';



//const image = { uri: "https://reactjs.org/logo-og.png" };
class login extends Component {


  constructor(props) {
    super(props)
    this.state = {
      credenciales: [],
      username: "us",
      password: "pas",
      loading: true
    };
  };



  fetchData = async () => {
    const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/credenciales');
    const credenciales = await response.json();
    this.setState({ credenciales: credenciales, loading: false });

  }
  componentDidMount() {
    this.fetchData();
  }
  saludo = () => {
    Alert.alert("Wena CT");
    this.props.navigation.navigate('Home')
  }
  entrar = () => {
    this.props.navigation.navigate('Home');
    //this.props.navigation.navigate('ventas')
    //console.log("paso aqui :c");    
  }
  cambiar = () => {
    this.props.navigation.navigate('Home');
  }
  verificar = () => {
    const usuarios = this.state.credenciales;
    const usuarioingresado = this.state.username;
    const contraseñaingresada = this.state.password;
    var correcto = 0;
    var autorizado = 0;
    for (var i = 0; i < usuarios.length; i++) {
      if (usuarioingresado == usuarios[i].umovil) {
        if (contraseñaingresada == usuarios[i].cmovil && usuarios[i].rol == "PERSONAL") {
          this.props.navigation.navigate('Home', usuarios[i]);
          alert("Bienvenido!" + " " + usuarios[i].umovil);
          correcto = 1;
          break;
        } else if (usuarios[i].rol != "PERSONAL") {
          alert("Usuario no autorizado!")
          correcto = 1;
        } else {
          alert("Contraseña incorrecta!");
          correcto = 1;
        }
      }
    }
    if (correcto == 0) {
      alert("usuario y contraseña incorrecta!")
    }
  }
  render() {
    return (
      <View style={styles.container}>
        <ImageBackground source={require("../assets/fondologin.jpg")} style={styles.imagen}>
          <View style={[styles.body, styles.negrita]}>
            <Text style={{ marginTop: 40, fontSize: 40, color: 'white' }}>LOGIN</Text>
          </View>
          <View>
            <Input id="usuarioingres1" placeholder={"Usuario"} style={styles.textinput} onChangeText={(text) => this.setState({ username: text })} />
            <Input secureTextEntry={true} id="passingres1" placeholder={"Contraseña"} style={styles.textinput} onChangeText={(text) => this.setState({ password: text })} />
          </View>
          <View style={styles.buttoncontainer}>
            <TouchableOpacity style={styles.button1} onPress={this.verificar} >
              <Text style={styles.buttontext1}>Iniciar Sesion</Text>
            </TouchableOpacity>
          </View>
          <View style={styles.footer}>

          </View>
        </ImageBackground>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column'
  },
  icono: {
    marginLeft: -220,
    position: "absolute"
  },
  textinput: {
    backgroundColor: 'white',
    borderRadius: 30,
    paddingLeft: 10,
    marginHorizontal: 40,
    fontSize: 22,
    paddingVertical: 8,
    marginVertical: 5,

  },
  imagen: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center"
  },
  buttoncontainer: {
    flex: 5,
    flexDirection: 'column',
    justifyContent: "flex-start",
    alignItems: "center",

  },
  logo: {
    maxWidth: "85%",
    maxHeight: "60%",
    resizeMode: "contain",
    justifyContent: "flex-start",
    position: "relative",
  },
  button1: {
    elevation: 10,
    backgroundColor: "#009688",
    borderRadius: 10,
    paddingVertical: 10,
    paddingHorizontal: 40,
    marginVertical: 10,
    marginTop: 20,
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
  }

})

export default login