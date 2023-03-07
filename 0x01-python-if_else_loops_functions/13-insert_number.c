#include <stdlib.h>
#include "lists.h"

/**
 * inser_node - function in C that inserts a 
 * number into a sorted singly linked list
 *
 * @head: pointer to the head of the list
 * @number: position where the node is to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number);
