
import React, { Component } from 'react';
import { Platform, StyleSheet, Text, View, FlatList, Image, Card, TouchableOpacity, Alert } from 'react-native';
import { ceil } from 'react-native-reanimated';
export default class App extends Component {

  state = {
    data: [],
    loading: true
  }



  /*state ={
    data:[{nombre:"jordan Cardenas Mercado",rut:"123456",telefono:"20254825",edad:"14"},{nombre:"fabian cardenas",rut:"20042236",telefono:"987654",edad:"15"},]
  }*/
  /*"nombre":["fabian"],
   "catidad":["2"]*/


  //obtiene los datos desde una api la cual saca los datos de la base de datos y los presenta en la url de fetch
  fetchData = async () => {
    const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/visitas')
    const paciente = await response.json();
    this.setState({ data: paciente, loading: false });
  }
  componentDidMount() {
    this.fetchData();
  }
  //<Image style = {styles.logo} source = {require("../assets/perfil.png")}></Image>
  render() {
    return (
      <View >
        <Text>{this.state.data.apellido1}</Text>
        <FlatList
          data={this.state.data}
          keyExtractor={(item, index) => index.toString()}
          renderItem={({ item }) =>
            <View style={{ backgroundColor: '#abc123', padding: 10, margin: 10 }}>
              <TouchableOpacity onPress={() => this.props.navigation.navigate('Paciente', item)} >
                <Text style={styles.textItem}>{item.nombre} {item.apellido1}</Text>
                <Text style={styles.textItem}>{item.rut} </Text>

              </TouchableOpacity>

            </View>
          }
        />

      </View>
    );
  }
}
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  header: {
    flexDirection: 'row',
  },
  input: {
    marginLeft: 10,
    marginTop: 10,
    width: 250,
    height: 40,
    borderColor: 'gray',
    borderWidth: 1
  },
  button: {
    alignItems: 'center',
    width: 70,
    height: 40,
    backgroundColor: '#79D0FF',
    borderRadius: 2,
    marginLeft: 10,
    marginTop: 10
  },
  textButton: {
    marginTop: 10,
  },
  listItem: {
    flexDirection: 'row',
    alignItems: 'center',
    width: 350,
    height: 70,
    borderBottomWidth: StyleSheet.hairlineWidth,
  },
  buttonItem: {
    alignItems: 'center',
    width: 70,
    height: 40,
    backgroundColor: '#FF7979',
    borderRadius: 2,
    marginLeft: 10,
  },
  textItem: {
    color: '#fff',
    paddingLeft: 10,
    textTransform: "uppercase",
    fontWeight: "bold",
    fontSize: 18,
    alignItems: "center",
    justifyContent: "center"

  },
  logo: {
    width: 50,
    height: 50,
    resizeMode: "contain",
    marginTop: -30,

  },
});