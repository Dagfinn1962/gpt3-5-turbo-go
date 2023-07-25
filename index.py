package main

import (
	gpt35 "github.com/AlmazDelDiablo/gpt3-5-turbo-go"
)

func main() {
	c, _ := gpt35.NewClient("sk-xxxxxxxxxxxxxxxxxxxx")
	req := &gpt35.Request{
		Model: gpt35.ModelGpt35Turbo,
		Messages: []*gpt35.Message{
			{
				Role:    gpt35.RoleUser,
				Content: "Hello",
			},
		},
	}

	resp, err := c.GetChat(req)
	if err != nil {
		panic(err)
	}

	println(resp.Choices[0].Message.Content)
	println(resp.Usage.PromptTokens)
	println(resp.Usage.CompletionTokens)
	println(resp.Usage.TotalTokens)
}
