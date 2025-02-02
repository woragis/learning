import { View, Text, TouchableOpacity, StyleSheet } from 'react-native'
import React from 'react'

interface ModalProps {
  title: string
  message: string
  buttonMessage: string
}

export default function Modal({ title, message, buttonMessage }: ModalProps) {
  return (
    <View style={styles.modal}>
      <Text style={styles.title}>{title}</Text>
      <View style={styles.body}>
        <Text style={styles.message}>{message}</Text>
        <View style={styles.buttonsContainer}>
          <TouchableOpacity style={styles.button}>
            <Text>Cancel</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button}>
            <Text>{buttonMessage}</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  )
}

const styles = StyleSheet.create({
  modal: {},
  title: {},
  body: {},
  message: {},
  buttonsContainer: {},
  button: {},
})
