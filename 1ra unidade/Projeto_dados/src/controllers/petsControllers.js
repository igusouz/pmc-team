import pets from "../models/pets.js";
import mongoose from 'mongoose';

class PetsController {

  // Listar todos os pets
  static async listarPets(req, res) {
    try {
      const listarPets = await pets.find({});
      res.status(200).json(listarPets);
    } catch (erro) {
      res.status(500).json({ message: `Erro ao listar pets - ${erro.message}` });
    }
  }

  // Listar pet por ID
  static async listarPetsPorId(req, res) {
    try {
      const id = req.params.id;

      // Validação do ID
      if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(400).json({ message: "ID inválido para o pet" });
      }

      const petsEncontrado = await pets.findById(id);
      if (!petsEncontrado) {
        return res.status(404).json({ message: "Pet não encontrado" });
      }

      res.status(200).json(petsEncontrado);
    } catch (erro) {
      res.status(500).json({ message: `Erro ao listar pet - ${erro.message}` });
    }
  }

  // Atualizar pet
  static async atualizarPets(req, res) {
    try {
      const id = req.params.id;

      // Validação do ID
      if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(400).json({ message: "ID inválido para o pet" });
      }

      const petAtualizado = await pets.findByIdAndUpdate(id, req.body, { new: true });
      if (!petAtualizado) {
        return res.status(404).json({ message: "Pet não encontrado" });
      }

      res.status(200).json({ message: "Pet atualizado com sucesso!", pet: petAtualizado });
    } catch (erro) {
      res.status(500).json({ message: `Erro ao atualizar pet - ${erro.message}` });
    }
  }

  // Cadastrar pet
  static async cadastrarPets(req, res) {
    try {
      const petsNovo = await pets.create(req.body);
      res.status(201).send({ message: 'Pet cadastrado com sucesso!', pets: petsNovo });
    } catch (erro) {
      res.status(500).json({ error: `${erro.message} - Falha ao cadastrar pet` });
    }
  }

  // Excluir pet
  static async excluirPets(req, res) {
    try {
      const id = req.params.id;

      // Validação do ID
      if (!mongoose.Types.ObjectId.isValid(id)) {
        return res.status(400).json({ message: "ID inválido para o pet" });
      }

      const petExcluido = await pets.findByIdAndDelete(id);
      if (!petExcluido) {
        return res.status(404).json({ message: "Pet não encontrado" });
      }

      res.status(200).json({ message: "Pet excluído com sucesso!" });
    } catch (erro) {
      res.status(500).json({ message: `Erro ao excluir o pet - ${erro.message}` });
    }
  }
}

export default PetsController;
