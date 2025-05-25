let itens = [];
let sequencial = 1;
const precos = {
    mussarela: 30,
    bacon: 32,
    calabresa: 32,
    calabresacatupiry: 35,
    calabresapaulistana: 30,
    milho: 30,
    frango: 35,
    frangocatupiry: 40,
    franbacon: 40,
    frangocaipira: 35,
    carijo: 40,
    presunto: 35,
    bauru: 40,
    portuguesa: 40,
    sobrado: 40,
    nordestina: 40,
    cocacola1L: 10,
    cocacola2L: 15,
    guaranaantarctica1L: 10,
    guaranaantarctica2L: 15,
    guaranasantajoana2L: 7
};

// Mostrar/ocultar campo de taxa de entrega
document.querySelectorAll('input[name="tipoPedido"]').forEach(radio => {
    radio.addEventListener('change', function() {
        document.getElementById('campoEntrega').style.display = 
            this.value === 'entrega' ? 'block' : 'none';
        atualizarListaItens();
    });
});

document.getElementById('sabor1').addEventListener('change', function() {
    const sabor2 = document.getElementById('sabor2');
    const currentValue = sabor2.value;
            
    // Mantém o valor atual se ainda estiver disponível
    sabor2.innerHTML = document.getElementById('sabor1').innerHTML;
    sabor2.value = sabor2.querySelector(`option[value="${currentValue}"]`) ? currentValue : sabor2.options[0].value;
});

function abrirModal() {
    document.getElementById('modalItem').style.display = 'block';
}

function fecharModal() {
    document.getElementById('modalItem').style.display = 'none';
}

function atualizarCamposPizza() {
    const produto = document.getElementById('produto').value;
    const camposPizza = document.getElementById('camposPizza');
    camposPizza.style.display = produto === 'pizza' ? 'block' : 'none';
}

function adicionarItem() {
    const produto = document.getElementById('produto').value;
    let descricao = '';
    let valorUnitario = 0;

    if (produto === 'pizza') {
        const sabor1 = document.getElementById('sabor1').value;
        const sabor2Element = document.getElementById('sabor2');
        const sabores = document.querySelector('input[name="sabores"]:checked').value;

        descricao = `Pizza ${formatarSabor(sabor1)}`;
        valorUnitario = precos[sabor1];

        if (sabores === '2') {
            const sabor2 = sabor2Element.value;
            descricao += ` + ${formatarSabor(sabor2)}`;
            valorUnitario = ((precos[sabor1]/2) + (precos[sabor2]/2));
        }
    } else {
                descricao = formatarProduto(produto);
                valorUnitario = precos[produto];
    }

    const quantidade = parseInt(document.getElementById('quantidade').value);

    itens.push({
        sequencial: sequencial++,
        descricao: descricao,
        quantidade: quantidade,
        valorUnitario: valorUnitario,
        total: quantidade * valorUnitario
    });

    atualizarListaItens();
    fecharModal();
}

function atualizarListaItens() {
    const tbody = document.querySelector('#itensPedido tbody');
    tbody.innerHTML = '';
    let totalPedido = 0;

    itens.forEach(item => {
        totalPedido += item.total;
        tbody.innerHTML += `
            <tr>
                <td>${item.sequencial}</td>
                <td>${item.descricao}</td>
                <td>${item.quantidade}</td>
                <td>R$ ${item.valorUnitario.toFixed(2)}</td>
                <td>R$ ${item.total.toFixed(2)}</td>
                <td><span class="remove-item" onclick="removerItem(${item.sequencial})">✖</span></td>
            </tr>
        `;
    });

    // Adiciona taxa de entrega se for pedido de entrega
    const tipoPedido = document.querySelector('input[name="tipoPedido"]:checked').value;
    if (tipoPedido === 'entrega') {
        const taxa = parseFloat(document.getElementById('taxaEntrega').value);
        totalPedido += taxa;
    }

    document.getElementById('totalPedido').textContent = totalPedido.toFixed(2);
}

function formatarSabor(sabor) {
    return sabor.charAt(0).toUpperCase() + sabor.slice(1);
}

function formatarProduto(produto) {
    return produto.charAt(0).toUpperCase() + produto.slice(1);
}

function removerItem(seq) {
    itens = itens.filter(item => item.sequencial !== seq);
    atualizarListaItens();
}