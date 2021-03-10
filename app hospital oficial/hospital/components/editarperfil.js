import React, { Component } from 'react'
import { StyleSheet, Text, View, Image, Button, Alert, TouchableOpacity, TextInput, TouchableHighlight } from 'react-native'
import { Input } from 'react-native-elements'
import { createAppContainer } from 'react-navigation'
import { createStackNavigator } from 'react-navigation-stack'


class ItemStock extends Component {
    constructor(props) {
        super(props)
        this.state = {
            personal: [],
            especialidad: [],
            telefono: "",
            email: "",
            loading: true
        };
    };

    fetchData = async () => {
        /*let myHeaders = new Headers();
        var data = {username: '3'}
        const options = {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers: {
                'Content-Type': 'application/json'
            }
        }*/
        const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/perfil');
        const response1 = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/personal');
        const personal = await response.json();
        const especialidad = await response1.json();
        const id_personal = this.props.navigation.state.params.usuario_id;
        for (var i = 0; i < personal.length; i++) {
            if (personal[i].id == id_personal) {
                this.setState({ personal: personal[i] });
                this.setState({ email: personal[i].email })
            }
        }
        for (var i = 0; i < especialidad.length; i++) {
            if (especialidad[i].id_perfil_id == id_personal) {
                this.setState({ especialidad: especialidad[i], loading: false });

            }
        }
        this.setState({ telefono: this.props.navigation.state.params.tel })

    }
    UpdateData = async () => {
        var data = { telefono: this.state.telefono, email: this.state.email, id: this.props.navigation.state.params.usuario_id }
        const options = {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers: {
                'Content-Type': 'application/json'
            }
        }
        alert("Datos Actualizados!, reinicie la aplicacion para hacer efectivos los cambios")
        this.props.navigation.navigate('Perfil', this.props.navigation.state.params)
        const response = await fetch('http://ec2-18-220-31-255.us-east-2.compute.amazonaws.com:1348/perfiledit', options);


    }
    componentDidMount() {
        this.fetchData();
    }

    saludo = () => { Alert.alert("Wena CTM!") }
    render() {
        return (
            <View>
                <View style={styles.columna}>
                    <Image style={styles.logo} source={require("../assets/perfil.png")}></Image>
                    <Text style={styles.texto}> {this.state.personal.first_name} {this.state.personal.last_name}</Text>
                    <Text style={styles.texto}>{this.state.especialidad.especialidad}</Text>
                </View>
                <Text style={styles.texto1}> {this.state.especialidad.rut} </Text>
                <TextInput onChangeText={(text) => this.setState({ telefono: text })} style={styles.input1} defaultValue={this.props.navigation.state.params.tel}></TextInput>
                <TextInput onChangeText={(text) => this.setState({ email: text })} style={styles.input2} defaultValue={this.state.personal.email}></TextInput>
                <TouchableOpacity style={styles.button1} onPress={this.UpdateData}>
                    <Text style={styles.buttontext1} onPress={this.UpdateData}>Guardar Cambios</Text>
                </TouchableOpacity>
                <View style={styles.container}>
                    <Image style={styles.logo1} source={require("../assets/logo.png")}></Image>
                </View>
            </View>

        )
    }
}
export default ItemStock
const styles = StyleSheet.create({
    columna: {
        flexDirection: "row",
        flex: 1,
        alignItems: "center",
        marginTop: 100
    },
    input: {
        borderBottomColor: 'black',
        borderBottomWidth: 1,
        fontSize: 20,
        maxWidth: "45%",
        marginHorizontal: 15
    },
    input1: {
        borderBottomColor: 'black',
        borderBottomWidth: 1,
        fontSize: 20,
        maxWidth: "90%",
        marginHorizontal: 15,
        marginTop: 40
    },
    input2: {
        borderBottomColor: 'black',
        borderBottomWidth: 1,
        fontSize: 20,
        maxWidth: "90%",
        marginHorizontal: 15,
        marginTop: 15
    },
    container: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: "flex-start",
        alignItems: "center",
    },
    texto: {
        paddingHorizontal: 10,
        textAlign: "center",
        fontSize: 20,
    },
    texto1: {
        paddingHorizontal: 15,
        fontSize: 20,
        paddingTop: 10
    },
    logo: {
        width: 150,
        height: 150,
        marginLeft: 20,
        marginVertical: 15
    },
    logo1: {
        width: 150,
        height: 150,
        alignItems: "center",
        marginTop: -10
    },
    form: {
        backgroundColor: 'white',
        marginVertical: 15,
        marginHorizontal: 10

    },
    textform: {
        paddingVertical: 5,
        paddingLeft: 5

    },
    titleitem: {
        marginBottom: -10
    },
    button1: {
        elevation: 10,
        backgroundColor: "#009688",
        borderRadius: 10,
        paddingVertical: 10,
        paddingHorizontal: 10,
        marginVertical: 10,
        marginHorizontal: 40,
        minWidth: "70%",
        borderRadius: 30
    },
    buttontext1: {
        fontSize: 18,
        color: "#fff",
        fontWeight: "bold",
        alignSelf: "center",
        textTransform: "uppercase"
    }

})